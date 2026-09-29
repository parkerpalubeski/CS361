from collections import deque


#Inputs: pairs (list)
#Description: This function converts pairs, a list of edges, to an adjacency matrix named links, in which each entry's keyname is a "source" node and the values are the nodes that the keyname node is connected to
#Outputs: links (dict)
def build_links(pairs):
    links = {}
    for a, b in pairs:
        links.setdefault(a, set()).add(b)
        links.setdefault(b, set()).add(a)
    return links

#Inputs: links (dict), start(char?), seen(set)
#Description: Searches the links data structure to determine all nodes that are connected to the start node. Returns the specific cluster searched as "group"
#Outputs: group (list)
def sweep(links, start, seen):
    group = []
    pending = deque([start])
    seen.add(start)
    while pending:
        n = pending.popleft()
        group.append(n)
        for m in links[n]:
            if m not in seen:
                seen.add(m)
                pending.append(m)
    return group

#Inputs: pairs (list)
#This function calls build_links to convert the edge list to an adjacency matrix, then iterates through each node and grouping nodes by adjacency (in other words, "clusters")
#Outputs: Groups (list)
def clusters(pairs):
    links = build_links(pairs)
    seen = set()
    groups = []
    for n in links:
        if n not in seen:
            groups.append(sweep(links, n, seen))
    return groups

#Inputs: pairs (list)
#This function calls clusters() to return to groups, then returns the largest list in groups (indicative of the largest graph by edge count) 
#Outputs: list
def biggest(pairs):
    groups = clusters(pairs)
    return max(groups, key=len)


#Inputs: None
#Description: This function initializes a list of tuples that contain edges in a graph (or technically a few separate graphs). Each tuple is an edge, and it contains the nodes (e.g. 'a' or 'b') that said edge connects to. It then calls the above functions to modify before printing out each individual graph and the largest graph by number of edges.
#Outputs: None
def main():
    pairs = [                                               #initializing the list of tuples
        ("a", "b"), ("b", "c"), ("c", "a"),
        ("d", "e"),
        ("f", "g"), ("g", "h"), ("h", "i"), ("i", "f"),
        ("j", "j"),
    ]
    groups = clusters(pairs)
    for g in groups:
        print(sorted(g))
    print(sorted(biggest(pairs)))


if __name__ == "__main__":
    main()