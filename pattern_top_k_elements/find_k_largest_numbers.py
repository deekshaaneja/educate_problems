from heapq import *

def find_k_largest_numbers(nums, k):
    min_heap = []
    for i in range(len(nums)):
        if len(min_heap) < k:
            heappush(min_heap, nums[i])
        else:
            heappushpop(min_heap, nums[i])
    return min_heap

def main():
    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))

main()