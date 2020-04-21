def remove_duplicates(arr):
    low, high = 0, 1
    while high < len(arr):
        if arr[high] == arr[low]:
            pass
        else:
            arr[low+1], arr[high] = arr[high], arr[low+1]
            low += 1
        high += 1
    return arr[:low+1]

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
# print(remove_duplicates1([2, 3, 3, 3, 6, 9, 9]))


