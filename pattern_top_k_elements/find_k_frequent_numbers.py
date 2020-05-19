from heapq import *


def find_k_frequent_numbers(nums, k):
    freq_map = {}
    for number in nums:
        if number in freq_map:
            freq_map[number] += 1
        else:
            freq_map[number] = 1
    min_heap = []
    for num, freq in freq_map.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)
    min_heap_sorted = sorted(min_heap, key = lambda x:x[1], reverse=True)
    return min_heap

def main():

    print("Here are the K frequent numbers: " +
            str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11, 11, 12, 12], 2)))

    print("Here are the K frequent numbers: " +
            str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()