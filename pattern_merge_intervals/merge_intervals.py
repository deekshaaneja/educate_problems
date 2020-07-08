def merge_intervals(arr):
    res = []
    i = 0
    while i < len(arr):
        if len(res) > 0:
            if res[-1][1] >= arr[i][0]:
                min_elem = min(res[-1][0], arr[i][0])
                max_elem = max(res[-1][1], arr[i][1])
                elem = [min_elem, max_elem]
                res[-1] = elem
                i += 1
            else:
                res.append(arr[i])
                i += 1
        else:
            res.append(arr[i])
            i += 1
    return res

def main():
    print("Merged intervals: ", merge_intervals([[1, 4], [2, 5], [7, 9]]))
    print("Merged intervals: ", merge_intervals([[2, 4], [5, 9], [6, 7]]))
    print("Merged intervals: ", merge_intervals([[1, 4], [2, 6], [3, 5]]))


main()