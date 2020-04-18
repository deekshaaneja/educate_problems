import math

def max_sub_array_of_size_k(k, arr):
    window_start = 0
    current_sum = 0
    max_sum = -1*math.inf
    for window_end in range(len(arr)):
        current_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[window_start]
            window_start += 1
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()