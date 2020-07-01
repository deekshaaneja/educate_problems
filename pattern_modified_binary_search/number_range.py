def find_range(arr, key):
    left = 0
    right = len(arr) -1
    result = [-1, -1]
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == key:
            i = mid
            while arr[i] == key:
                i = i-1
            j = mid
            while arr[j] == key:
                j = j+1
            result = [i+1, j-1]
            return result
        elif key > arr[mid]:
            left = mid+1
        elif key < arr[mid]:
            right = mid-1
    return result

def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
