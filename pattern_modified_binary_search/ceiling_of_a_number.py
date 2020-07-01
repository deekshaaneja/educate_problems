
def search_ceiling_of_a_number(arr, key):
    left = 0
    right = len(arr) -1
    if key > arr[right] -1:
        return -1
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
    return left

def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()