def max_sub_array_of_size_k(k, arr):
    currentSum = maxSum = 0
    ls = []
    for i in range(len(arr)):
        currentSum = sum(ls)
        if currentSum > maxSum:
            maxSum = currentSum
        if len(ls) == k:
            ls.pop(0)
        ls.append(arr[i])
    return ls, maxSum

print(max_sub_array_of_size_k(3,[2, 1, 5, 1, 3, 2]))
