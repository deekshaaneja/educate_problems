def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    if key > arr[n-1]:
        return -1
    
    start, end = 0, n-1
    while start <= end:
        mid = start + (end-start) // 2
        if key < arr[mid]:
            end = mid -1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid

    return start

def main():
    # print(search_ceiling_of_a_number([4, 6, 10], 6))
    # print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    # print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
