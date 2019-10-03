def pair_with_targetsum(ls,target):
    pair_set = set()
    out = []
    for num in ls:
        num_target = target-num
        if num_target in pair_set:
            out.append(ls.index(num_target))
            out.append(ls.index(num))
            return out
        else:
            pair_set.add(num)

print(pair_with_targetsum([1, 2, 3, 4, 6], 6))