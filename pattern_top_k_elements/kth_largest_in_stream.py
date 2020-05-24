from heapq import *

class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.min_heap = []
        for i in range(len(nums)):
            if len(self.min_heap) < self.k:
                heappush(self.min_heap, nums[i])
            else:
                heappushpop(self.min_heap, nums[i])

    def add(self, num):
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, num)
        else:
            heappushpop(self.min_heap, num)
        return self.min_heap[0] 

def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()



