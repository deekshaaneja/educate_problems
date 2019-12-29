def max_sub_array_of_size_k(k, arr):
    window_start = 0
    max_sum = 0
    curr_sum = 0
    for window_end in range(len(arr)):
        if window_end < k:
            curr_sum += arr[window_end]
        else:
            curr_sum -= arr[window_start]
            curr_sum += arr[window_end]
            window_start += 1
        max_sum = max(max_sum, curr_sum)
    return max_sum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()