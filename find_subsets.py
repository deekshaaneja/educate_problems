def find_subsets(nums):
    subsets = []
    subsets.append([])
    for elem in nums:
        n = len(subsets)
        for i in range(n):
            set = list(subsets[i])
            set.append(elem)
            subsets.append(set)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
