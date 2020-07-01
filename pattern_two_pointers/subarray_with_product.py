from collections import deque

def find_subarrays(arr, target):
    # arr.sort()
    window_start = 0
    curr_product = 1
    res = []
    for window_end in range(len(arr)):
        curr_product = curr_product*arr[window_end]
        if curr_product == 1:
            while window_start < window_end:
                res.append(arr[window_start: window_end])
                window_start += 1
        else:
            while curr_product >= target and window_start < len(arr):
                curr_product = curr_product / arr[window_start]
                window_start += 1
            temp_list = deque()
            for i in range(window_end, window_start-1, -1):
                temp_list.appendleft(arr[i])
                res.append(list(temp_list))
    return res

def main():
    # print(find_subarrays([2, 5, 3, 10], 30))
    # print(find_subarrays([8, 2, 6, 5], 50))
    # print(find_subarrays([10,5,2,6], 100))
    # print(find_subarrays([1, 2, 3], 0))
    print(find_subarrays([1, 1, 1], 2))


main()
