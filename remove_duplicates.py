def remove_duplicates(arr):
    last_elem = 0
    length = 0
    i = 0
    while i<len(arr):
        if arr[i] == last_elem:
            length +=1
        else:
            last_elem = arr[i]
        i+=1
    return i-length

def remove_duplicates1(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1
    i = 1
    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates1([2, 3, 3, 3, 6, 9, 9]))


