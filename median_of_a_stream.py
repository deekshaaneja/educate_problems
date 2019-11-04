from heapq import *

class MedianOfAStream:
    min_heap = []
    max_heap = []

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >=num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0]/2 + self.min_heap[0]/2
        return -self.max_heap[0]


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