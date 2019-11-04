def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        if window_end-window_start < k:
            window_sum += arr[window_end]
        else:
            window_sum = window_sum - arr[window_start] + arr[window_end]
            max_sum = max(max_sum, window_sum)
            window_start += 1
        
    return max_sum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()