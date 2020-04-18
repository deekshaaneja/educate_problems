def search_ceiling_of_a_number(arr, key):
    start = 0
    end = len(arr) - 1
    last_num = arr[start]
    if key < arr[0]:
        return 0
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            if last_num < key:
                return mid
            end = mid - 1
        last_num = arr[mid]
    return -1

def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()