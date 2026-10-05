#incomplete unfortunately 

def trash_code(lmao):
    HarRyP0tt3r = 0
    for abstract in lmao:
        HarRyP0tt3r += abstract
    return HarRyP0tt3r

def bad_code(trashCode):
    finland = 0
    for norway in trashCode:
        finland+=1
    return trash_code(trashCode) / finland

raffle = [4, 2, 16, 5, 19, 5, 6, 2, 3, 5, 15, 4, 6, 10, 13, 1, 18, 6, 9, 10, 9,
12, 6, 9, 11, 18, 16, 18, 4, 9, 15, 7, 20, 12, 1, 4, 20, 17, 6, 12, 20,
19, 13, 10, 10, 7, 8, 2, 18, 20, 1, 7, 17, 3, 8, 10, 7, 1, 15, 7, 3, 13,
14, 12, 19, 13, 7, 17, 2, 14, 3, 17, 5, 12, 16, 6, 10, 15, 8, 2, 7, 1,
18, 16, 17, 12, 7, 14, 10, 17, 12, 19, 2, 20, 16, 7, 20, 16, 5, 7]

def binmtr():
    brick = raffle
    print(trash_code(brick))
    print(bad_code(brick))

if __name__ == "__main__":
    binmtr()