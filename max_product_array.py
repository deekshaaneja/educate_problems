import math

def find_max_product(arr):
    window_start = 0
    window_end = 0
    curr_product = max_product = -1 * math.inf
    curr_product, prev_elem = 1, 1
    
    for window_end in range(window_start, len(arr)):
        curr_product = curr_product / prev_elem
        curr_product = curr_product * arr[window_end]
        max_product = max(max_product, curr_product)
        if window_end - window_start > 2:
            window_start += 1
        prev_elem = arr[window_start]
    return max_product

arr = [1, 4, 3, 6, 7, 0]
arr.sort()
print(find_max_product(arr))
