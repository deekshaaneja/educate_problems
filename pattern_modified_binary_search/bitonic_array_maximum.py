def find_max_in_bitonic_array(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if mid > 0 and mid < len(arr) - 1:
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return arr[mid]
            elif arr[mid+1] > arr[mid]:
                left = mid+1
            else :
                right = mid-1
        elif mid == 0:
            return arr[mid]
        elif mid == len(arr) - 1:
            return arr[len(arr) - 1]
    return None


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()