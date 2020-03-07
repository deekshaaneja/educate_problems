from heapq import *

def find_k_largest_numbers(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])
    return min_heap

def  find_k_largest_numbers_heapify(nums, k):
    # max_heap = heapify(nums)
    largest_k_nums = nlargest(3, nums)
    return largest_k_nums

def main():

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)) + " " +
        str(find_k_largest_numbers_heapify([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)) + " " +
        str(find_k_largest_numbers_heapify([5, 12, 11, -1, 12], 3)))

main()