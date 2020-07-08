

# [1, 1, 2, 7, 3, 5]

def merge(lsA, lsB):
    lsC = [elem for elem in lsB if elem not in lsA] + lsA
    return lsC


def main():
    lsA = [1, 1, 2, 7]
    lsB = [1, 1, 3, 5, 7]
    print(merge(lsA, lsB))

main()



