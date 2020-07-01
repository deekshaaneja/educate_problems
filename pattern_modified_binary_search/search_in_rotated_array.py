def search_rotated_array(arr, key):
    left = 0
    right = len(arr) -1
    isAscending = True
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == key:
            return mid
        if arr[left] < arr[mid]:
            if key > arr[left] and key <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if key > arr[mid] and key <= arr[right]:
                left = mid + 1
            else:
                right = mid -1
    return -1 
        

def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()