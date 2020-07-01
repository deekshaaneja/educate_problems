import math
from heapq import *

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self):
        distance = math.sqrt(self.x * self.x + self.y * self.y)
        return distance

    def __lt__(self, other):
        return self > other
    
    def print_point(self):
        return (self.x, self.y)

def find_closest_points(points, k):
    max_heap = []
    result = []
    for point in points:
        if len(max_heap) < k:
            heappush(max_heap, (-1 * point.distance(), point))
        else:
            heappushpop(max_heap, (-1 *point.distance(), point))
    for elem in max_heap:
        result.append(elem[1].print_point())
    return result

    
def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", result)
    # for point in result:
    #     point.print_point()


main()