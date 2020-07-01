from heapq import *


class medianOfAStreamClass:

    def __init__(self):
        self.maxHeap = []  # containing first half of numbers
        self.minHeap = []  # containing second half of numbers

    def insert_num(self, num):
        if len(maxHeap) > 0 and num >= maxHeap[0]:
            heappush(self.minHeap, -num)
        else:
            heappush(self.maxHeap, num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        return -self.maxHeap[0] / 1.0
    


def main():
    medianOfAStream = medianOfAStreamClass()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()