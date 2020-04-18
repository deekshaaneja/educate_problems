import math

def smallest_subarray_with_given_sum(s, arr):
    window_start, window_end = 0, 0
    window_sum = 0
    min_window_len = math.inf
    result = []
    for window_end in range(len(arr)):
        if window_sum < s:
            window_sum += arr[window_end]
        else:
            window_sum = window_sum + arr[window_end]
            min_window_len = min(min_window_len, window_end-window_start)
            while window_sum - arr[window_start] >= s:
                window_sum -= arr[window_start]
                min_window_len = min(min_window_len, window_end-window_start)
                window_start += 1
    return min_window_len


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
