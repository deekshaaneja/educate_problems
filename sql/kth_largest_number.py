from heapq import *

class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.nums = nums

    def add(self, num):
        self.nums += [num]
        min_heap = []
        for i in range(self.k):
            heappush(min_heap, self.nums[i])
        for i in range(self.k, len(self.nums)):
            heappushpop(min_heap, self.nums[i])
        return min_heap[0]


def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()