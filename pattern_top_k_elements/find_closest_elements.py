from heapq import *
import math

def find_closest_elements(arr, K, X):
    max_heap = []
    for i in range(len(arr)):
        if len(max_heap) < K:
            heappush(max_heap, (-1*abs(X-arr[i]), arr[i]))
        else:
            heappushpop(max_heap, (-1*abs(X-arr[i]), arr[i]))
    return [elem[1] for elem in max_heap]

def main():
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
            str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
