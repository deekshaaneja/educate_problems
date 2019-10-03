def smallest_subarray_with_given_sum(s, arr):
    ls = []
    while len(arr)>0:
        maxNum = max(arr)
        ls.append(maxNum)
        if sum(ls) >= s:
            return(len(ls))
        else:
            arr.remove(maxNum)

print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))
