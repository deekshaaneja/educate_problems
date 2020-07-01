def merge_sort(arr, start, end):
    if start == end:
        return [arr[start]]
    mid = start + (end-start)//2
    left = merge_sort(arr, start, mid)
    right = merge_sort(arr, mid+1, end)
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            output.append(right[j])
            j += 1
        else:
            output.append(left[i])
            i += 1
    if i == len(left):
        output += right[j:]
    else:
        output += left[i:]
    return output
    


print(merge_sort([6, 5, 8, 9, 10], 0, 4))
