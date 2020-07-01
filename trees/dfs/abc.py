import math
from heapq import *


def find_max_diff(ls, k):
    max_heap = []
    curr_min = math.inf
    curr_max = -math.inf
    for i in range(len(ls)):
        curr_max = max(curr_max, ls[i])
        curr_min = min(curr_min, ls[i])
        if len(max_heap) < k:
            heappush(max_heap, -ls[i])
        else:
            heappushpop(max_heap, -ls[i])
    print(max_heap)
    print(curr_max)
    return curr_max + max_heap[0]


ls = [10, 10, 10]
print(find_max_diff(ls, 2))