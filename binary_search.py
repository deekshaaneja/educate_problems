def binary_search(arr, key):
    start = 0
    end = len(arr) -1
    if arr[start] > arr[end]:
        is_ascending = False
    else:
        is_ascending = True
    if is_ascending == True:
        while end >= start:
            mid = start + (end - start) // 2
            if arr[mid] == key:
                return True
            elif arr[mid] > key:
                end = mid - 1
            elif arr[mid] < key:
                start = mid + 1
            # start += 1
            # end -= 1
    else:
        while end >= start:
            mid = start + (end - start) // 2
            if arr[mid] == key:
                return True
            elif arr[mid] < key:
                end = mid - 1
            elif arr[mid] > key:
                start = mid + 1
    return False


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()