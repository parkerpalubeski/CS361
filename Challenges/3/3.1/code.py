import struct
import zlib
import json
import time
import hmac
import hashlib


def handle_packet(data, conn, server):
    if len(data) < 12:
        server.logger.warning("short packet from %s", conn.addr)
        return

    magic, version, flags, msg_type, seq, payload_len = struct.unpack(">HBBHIH", data[:12])
    if magic != 0xCAFE:
        conn.close()
        return
    if version not in (3, 4):
        conn.send(struct.pack(">HBBH", 0xCAFE, 4, 0, 0xFFFF))
        return
    if seq <= conn.last_seq:
        return
    conn.last_seq = seq

    body = data[12:12 + payload_len]
    trailer = data[12 + payload_len:]

    # ones-complement 16-bit checksum
    total = 0
    for i in range(0, len(body) - 1, 2):
        total += (body[i] << 8) | body[i + 1]
    if len(body) % 2:
        total += body[-1] << 8
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    if (~total & 0xFFFF) != struct.unpack(">H", trailer[:2])[0]:
        server.metrics.increment("packets.bad_checksum")
        return

    if flags & 0x01:
        body = zlib.decompress(body)
    if flags & 0x02:
        sig = trailer[2:34]
        expected = hmac.new(conn.session_key, body, hashlib.sha256).digest()
        if not hmac.compare_digest(sig, expected):
            server.ban_list.add(conn.addr[0])
            conn.close()
            return

    if msg_type == 0x0001:  # LOGIN
        name_len = body[0]
        username = body[1:1 + name_len].decode("utf-8")
        token = body[1 + name_len:1 + name_len + 32].hex()
        row = server.db.execute(
            "SELECT id, banned, last_seen FROM players WHERE username = ? AND token = ?",
            (username, token),
        ).fetchone()
        if row is None or row[1]:
            conn.send(struct.pack(">HBBHB", 0xCAFE, version, 0, 0x8001, 0))
            return
        player = server.world.spawn_player(row[0], username)
        conn.player = player
        server.db.execute("UPDATE players SET last_seen = ? WHERE id = ?", (int(time.time()), row[0]))
        server.db.commit()
        server.broadcast_system_message(f"{username} has joined the game")
        conn.send(struct.pack(">HBBHBI", 0xCAFE, version, 0, 0x8001, 1, player.entity_id))

    elif msg_type == 0x0002:  # MOVE
        if conn.player is None:
            return
        x, y, z = struct.unpack(">fff", body[:12])
        packed_rot = struct.unpack(">H", body[12:14])[0]
        yaw = ((packed_rot >> 8) & 0xFF) * (360.0 / 256)
        pitch = (packed_rot & 0xFF) * (180.0 / 256) - 90.0
        dx, dy, dz = x - conn.player.x, y - conn.player.y, z - conn.player.z
        elapsed = time.time() - conn.player.last_move_time
        if (dx * dx + dy * dy + dz * dz) ** 0.5 > conn.player.max_speed * elapsed * 1.1:
            server.anticheat.flag(conn.player, "speed")
            conn.send(struct.pack(">HBBHfff", 0xCAFE, version, 0, 0x8002,
                                  conn.player.x, conn.player.y, conn.player.z))
            return
        conn.player.last_move_time = time.time()
        server.world.move_entity(conn.player, x, y, z, yaw, pitch)

    elif msg_type == 0x0003:  # CHAT
        if conn.player is None:
            return
        msg = json.loads(body.decode("utf-8"))
        text = msg.get("text", "")[:256]
        text = "".join(c for c in text if c.isprintable())
        for word in server.config["banned_words"]:
            text = text.replace(word, "*" * len(word))
        if msg.get("channel") == "team":
            server.chat.send_to_team(conn.player.team, conn.player.name, text)
        else:
            server.chat.broadcast(conn.player.name, text)

    else:
        server.logger.info("unknown msg_type 0x%04x from %s", msg_type, conn.addr)