# https://codepumpkin.com/trapping-rain-water-algorithm-problem/

import math

def find_qty(arr):
    qty = 0
    left_arr = [0] * len(arr)
    right_arr = [0] * len(arr)
    left_max = -math.inf
    right_max = -math.inf
    for i in range(len(arr)):
        left_max = max(arr[i], left_max)
        left_arr[i] = left_max
    for j in range(len(arr)-1, -1, -1):
        right_max = max(arr[j], right_max)
        right_arr[j] = right_max
    print(left_arr, right_arr)
    for i in range(len(arr)):
        curr_value = min(left_arr[i], right_arr[i])
        if curr_value >= arr[i]:
            qty += curr_value - arr[i]
    return qty

def main():
    print(find_qty([2, 0, 2]))
    print(find_qty([1, 4, 2, 5, 0, 6, 2,3, 4]))
    print(find_qty([0, 4, 5, 1]))

main()


