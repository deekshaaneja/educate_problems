from heapq import *

class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        