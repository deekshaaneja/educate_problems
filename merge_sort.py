
def merge_sort(arr, start, end):

    if start == end:
        return [arr[start]]
    mid = start + (end-start) // 2
    a = merge_sort(arr, start, mid) 
    b = merge_sort(arr, mid+1, end)

    result = []
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

print(merge_sort([13, 12, 17, 9], 0, 3))