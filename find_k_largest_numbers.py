from heapq import *

def find_k_largest_numbers(nums, k):
    k_heap = []
    # max_elem = 0
    for i in range(len(nums)):
        if len(k_heap) < k:
            # if nums[i] > max_elem:
            #     max_elem = nums[i]
            heappush(k_heap,nums[i])
        else:
            heap_root = heappop(k_heap)
            if nums[i] > heap_root:
                heappush(k_heap, nums[i])

    return k_heap

def main():

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()