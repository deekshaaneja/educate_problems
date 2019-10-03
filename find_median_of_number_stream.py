from heapq import *

class MedianOfAStream:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.N = 0

    def insertNum(self, num):
        if self.N % 2 == 0:
            heappush(self.maxHeap, -1*num)
            self.N += 1
            if len(self.minHeap) == 0:
                return
            if -1*self.maxHeap[0] > self.minHeap[0]:
                toMin = -1*heappop(self.maxHeap)
                toMax = heappop(self.minHeap)
                heappush(self.maxHeap,-1*toMax)
                heappush(self.minHeap,-toMin)
        else:
            toMin = -1* heappushpop(self.maxHeap,-1*num)
            heappush(self.minHeap,toMin)
            self.N +=1

    def getMedian(self):
        if self.N%2 == 0:
            median = -1*self.maxHeap[0] + self.minHeap[0] //2
        else:
            median = -1*self.maxHeap[0]
        return median


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insertNum(3)
    medianOfAStream.insertNum(1)
    print("The median is: " + str(medianOfAStream.getMedian()))
    medianOfAStream.insertNum(5)
    print("The median is: " + str(medianOfAStream.getMedian()))
    medianOfAStream.insertNum(4)
    print("The median is: " + str(medianOfAStream.getMedian()))

main()

