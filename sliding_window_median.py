from heapq import *

class sliding_median:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.k = 0

    def insert_num(self,nums):
        for num in nums:
            if self.k%2 == 0:
                heappush(self.maxHeap,-1*num)
                if len(self.minHeap) == 0:
                    return
                if -1*self.maxHeap[0] > self.minHeap[0]:
                    toMin = -1*heappop(self.maxHeap)
                    toMax = heappop(self.minHeap)
                    heappushpop(self.maxHeap, -1*toMax)
                    heappush(self.minHeap,toMin)
            else:
                toMin = -1 * heappushpop(self.maxHeap,-1*num)
                heappush(self.minHeap,toMin)
    def remove_num(self,nums,rem_num):
        if self.k%2 == 0:
            if rem_num in self.minHeap:
                heappop(self.minHeap,rem_num)
            else:
                heappop(self.maxHeap,rem_num)
            if -1*self.maxHeap[0] > self.minHeap[0]:
                toMin = -1*heappop(self.maxHeap)
                toMax = heappop(self.minHeap)
                heappushpop(self.maxHeap, -1*toMax)
                heappush(self.minHeap,toMin)


    def get_median(self):
        if self.k%2 == 0:
            median = (self.minHeap[0] + self.maxHeap)//2
        else:
            median = self.maxHeap[0]

