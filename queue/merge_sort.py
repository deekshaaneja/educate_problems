def merge_sort(arr, start, end):
    if start == end:
        return [arr[start]]

    mid = start + (end-start)//2
    left_arr = merge_sort(arr, start, mid)
    right_arr = merge_sort(arr, mid+1, end)
    output = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            output.append(left_arr[i])
            i += 1
        else:
            output.append(right_arr[j])
            j += 1
    if i == len(left_arr):
        output += right_arr[j:]
    elif j == len(right_arr):
        output += left_arr[i:]
    return output

print(merge_sort([6, 5, 8, 9, 10], 0, 4))
