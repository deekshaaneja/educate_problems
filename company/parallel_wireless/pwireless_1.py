



def bin_search(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == k:
            return k
        if k > arr[mid]:
            left = mid + 1
        elif k < arr[mid]:
            right = mid -1
    return -1


print(bin_search([1, 2, 3, 4, 5], 3))
print(bin_search([1, 2, 3, 4, 5], 6))
print(bin_search([1, 2, 3, 4, 5], 0))
print(bin_search([1, 2, 4, 5], 3))


# ls = [3, 4, 5, 1, 2]
# 2, 3, 4, 5, 1
# 5, 1, 2, 3, 4

def find_min_element(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] < arr[mid -1] and arr[mid] < arr[mid+1]:
            return mid
        elif arr[mid] < arr[right]:
            right = mid-1
        elif arr[left] < arr[mid]:
            left = mid+1
    return -1

print(find_min_element([3, 4, 5, 1, 2]))
print(find_min_element([3, 4, 5, 6, 7, 1, 2]))


        
    
