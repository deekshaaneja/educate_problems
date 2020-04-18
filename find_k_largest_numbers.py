from heapq import *

def find_k_largest_numbers(nums, k):
    min_heap = []
    for elem in nums:
        if len(min_heap) < k:
            heappush(min_heap, elem)
        else:
            heappushpop(min_heap, elem)
    return min_heap

def main():

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))

main()