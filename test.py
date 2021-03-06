
def merge_sort(arr, start, end):
    if start == end:
        return [arr[start]]
    
    result = []
    mid = start + (end-start) // 2

    a = merge_sort(arr, start, mid)
    b = merge_sort(arr, mid + 1, end)

    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i == len(a):
        result += b[j:]
    elif j == len(b):
        result += a[i:]
    return result

# print(merge_sort([1,3,5,2,45,21,31], 0, 6))
print(merge_sort([1,3,5,2], 0, 3))
    
