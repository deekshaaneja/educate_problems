from heapq import *


def find_k_frequent_numbers(nums, k):
    freq_map = {}
    max_k_elem = []
    for i in range(len(nums)):
        if nums[i] in freq_map:
            freq_map[nums[i]] += 1
        else:
            freq_map[nums[i]] = 1
    for elem in freq_map:
        if len(max_k_elem) < k:
            heappush(max_k_elem, (freq_map[elem], elem))
        else:
            heappushpop(max_k_elem, (freq_map[elem], elem))
    return max_k_elem

def main():

    print("Here are the K frequent numbers: " +
            str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11, 11, 12, 12], 2)))

    print("Here are the K frequent numbers: " +
            str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()