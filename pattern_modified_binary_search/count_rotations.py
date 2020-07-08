def count_rotations(arr):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]:
            return mid
        elif arr[mid] < arr[end]:
            end = mid-1
        else:
            start = mid+1
    return -1

def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()