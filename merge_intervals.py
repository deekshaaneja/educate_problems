def merge_intervals(ls):
    last_elem = None
    ls_out = []
    for elem in ls:
        curr_elem = elem
        if last_elem is not None:
            res = intersection(last_elem, curr_elem)
            if res == True:
                merged_elem = [last_elem[0], curr_elem[-1]]
                merged_elem = curr_elem
                ls_out.append(merged_elem)
            else:
                last_elem = curr_elem
                ls_out.append(curr_elem)
        else:
            last_elem = curr_elem
    return ls_out



def intersection(ls1, ls2):
    if ls1[-1] >= ls2[0]:
        return True
    return False

class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

# print(merge_intervals([[1,4], [2,5], [7,9]]))
print(merge_intervals([interval(1, 4), interval(2, 5), interval(7, 9)]))