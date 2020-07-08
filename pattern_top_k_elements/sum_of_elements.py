from heapq import *

def find_sum_elements(arr, k1, k2):
    max_heap = []
    max_k = max(k1, k2)
    min_k = min(k1, k2)
    diff_k = max_k - min_k
    res = []
    for i in range(len(arr)):
        if len(max_heap) < max_k:
            heappush(max_heap, -arr[i])
        else:
            heappushpop(max_heap, -arr[i])
    max_k_smallest_elem = - heappop(max_heap)
    sum = 0
    while diff_k != 0:
        elem = - heappop(max_heap)
        diff_k -= 1
        if diff_k != 0:
            sum += elem
    min_k_smallest_elem = elem
    print(min_k_smallest_elem, max_k_smallest_elem)
    return sum

def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
            str(find_sum_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
            str(find_sum_elements([3, 5, 8, 7], 1, 4)))


main()