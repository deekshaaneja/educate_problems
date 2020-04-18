from heapq import *

def find_k_frequent_numbers(nums, k):
    frequency = {}
    min_heap = []
    result = []
    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    for elem in frequency:
        elem_value = frequency[elem]
        if len(min_heap) < k:
            heappush(min_heap, (elem_value, elem))
        else:
            heappushpop(min_heap, (elem_value, elem))
    for num in min_heap:
        result.append(num[1])
    return result

def main():

    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " + str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

