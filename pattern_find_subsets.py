from copy import deepcopy

def find_subsets(nums):
    subsets = []
    subsets.append([])
    for i in range(len(nums)):
        # subsets.append([nums[i]])
        ls = []
        for elem in subsets:
            elem_1 = deepcopy(elem)
            elem_1.append(nums[i])
            if [nums[i]] not in ls and [nums[i]] not in subsets:
                ls.append([nums[i]])
            if elem_1 not in ls and elem_1 not in subsets:
                ls.append(elem_1)
        subsets += ls
    return subsets

def main():

    # print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()