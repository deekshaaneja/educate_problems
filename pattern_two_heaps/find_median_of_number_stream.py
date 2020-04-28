from heapq import *

class MedianOfaStream:
    def __init__(self, min_heap = [], max_heap = []):
        self.max_heap = []
        self.min_heap = []

    def insert_num(self, num):
        if not self.max_heap or -1 * self.max_heap[0] >= num:
            heappush(self.max_heap, -1 * num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -1 * heappop(self.max_heap)) 
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -1 * heappop(self.min_heap)) 

    def find_median(self):
        if len(self.min_heap) == len(self.max_heap):
            median = self.min_heap[0] / 2 - self.max_heap[0] /2
        else:
            median = -1 * self.max_heap[0] 
        return median

def main():
    medianOfAStream = MedianOfaStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()