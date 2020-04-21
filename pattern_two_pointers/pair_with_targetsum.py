def pair_with_targetsum(ls, target):
    seen = set()
    ls_pairs = []
    for num in ls:
        targer_num = target - num
        if targer_num in seen:
            ls_pairs.append((num, targer_num))
        else:
            seen.add(num)
    return ls_pairs

def pair_with_targetsum_return_index(ls, target):
    seen = {}
    ls_pairs = []
    for i in range(len(ls)):
        targer_num = target - ls[i]
        if targer_num in seen:
            ls_pairs.append((i, seen[targer_num]))
        else:
            seen[ls[i]] = i
    return ls_pairs

def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
    print(pair_with_targetsum_return_index([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum_return_index([2, 5, 9, 11], 11))


main()