####Kth Smallest Number in M Sorted Lists (Medium) ####

from heapq import *

def find_Kth_smallest(lists, k):
    minHeap = []
    max_index = 0
    for i in range(len(lists)):
        heappush(minHeap, (lists[i][0], i, lists[i]))
    
    numberCount, number = 0, 0
    while minHeap:
        number , i , list = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            return number
        if len(list) > i+1:
            heappush(minHeap, (list[i+1], i+1, list))
    return number

def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()


