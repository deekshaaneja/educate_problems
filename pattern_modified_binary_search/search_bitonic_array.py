
        
# [8, 6, 5]
def find_elem_bin(arr, key):
    left = 0
    right = len(arr) - 1
    isAscending = True
    if arr[-1] < arr[0]:
        isAscending = False
    while left <= right:
        mid = left + (right-left) // 2
        if key == arr[mid]:
            return mid
        if isAscending:
            if key > arr[mid]:
                left = mid+1
            else:
                right = mid-1
        else:
            if key > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return None

def bitonic_array_maximum(arr):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = left + (right-left) // 2
        if mid == 0 or mid == len(arr)-1:
            return mid
        else:
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid -1
    return -1
    
def search_bitonic_array(arr, key):
    max_elem_idx = bitonic_array_maximum(arr)
    arr1 = arr[:max_elem_idx+1]
    arr2 = arr[max_elem_idx+1:]
    # print(arr1, arr2)
    indx1 = find_elem_bin(arr1, key)
    if indx1 != None:
        return indx1
    indx2 = find_elem_bin(arr2, key)
    if indx2 != None:
        return indx2+max_elem_idx+1
    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))
    print(search_bitonic_array([10, 9, 8], 7))

main()