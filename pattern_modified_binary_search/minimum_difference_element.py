def search_min_diff_element(arr, key):
    left = 0
    right = len(arr) - 1
    if key > arr[right]:
        return arr[right]
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == key:
            return arr[mid]
        elif key > arr[mid]:
            left = mid + 1
        elif key < arr[mid]:
            right = mid -1
    x = abs(arr[left] - key)
    y = abs(arr[right] - key)
    return arr[left] if x < y else arr[right]

def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()