# [10, 6, 4], key = 10

def binary_search(arr, key):
    left = 0
    right = len(arr)
    isAscending = True
    if arr[-1] < arr[0]:
        isAscending = False
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == key:
            return mid
        if isAscending:
            if arr[mid] > key:
                right = mid -1
                # print(arr[right])
            else:
                left = mid + 1
        else:
            if arr[mid] < key:
                right = mid -1
            else:
                left = mid + 1
    return -1

def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
        

