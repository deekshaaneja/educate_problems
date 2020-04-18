from heapq import *

class MedianOfAStream:
    def __init__(self, minHeap = [], maxHeap = []):
        self.maxHeap = maxHeap
        self.minHeap = minHeap
    
    def insert_num(self, num):
        if len(self.maxHeap) == 0 or -num <= -self.maxHeap[0]:
            heappush(self.maxHeap, num)
        else:
            heappush(self.minHeap, -num)
        self.rebalance_heap()

    def find_median(self):
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        elif len(self.maxHeap) == len(self.minHeap):
            return (- self.minHeap[0] + self.maxHeap[0]) / 2

    def rebalance_heap(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            num = heappop(self.maxHeap)
            heappush(self.minHeap, -num)
        

def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()