import math
def search_min_diff_element(arr, key):
    n = len(arr)
    num1, num2 = 0, 0
    start, end = 0, n-1
    while start <= end:
        mid = start + (end-start) // 2
        if key < arr[mid]:
            end = mid -1
            num1 = mid
        elif key > arr[mid]:
            start = mid + 1
            num2= mid
        else:
            return arr[mid]
    return findmin_num(arr[num1], arr[num2], key)

def findmin_num(num1, num2, key):
    abs1 = abs(key - num1)
    abs2 = abs(key-num2)
    if abs1 < abs2:
        return num1
    else:
        return num2



def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
