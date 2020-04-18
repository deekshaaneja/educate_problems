
def subsets_with_duplicates(nums):
    # sort the numbers to handle duplicates
    nums.sort()
    subsets = []
    subsets.append([])
    start_index, end_index = 0, 0
    for i in range(len(nums)):
        start_index = 0
        if i > 0 and nums[i-1] == nums[i]:
            start_index = end_index + 1
        end_index = len(subsets) 
        for j in range(start_index, end_index):
            new_elem = list(subsets[j])
            new_elem.append(nums[i])
            subsets.append(new_elem)
    return subsets


def main():
    print("Here is the list of subsets: " + str(subsets_with_duplicates([1, 3, 3])))
    # print("Here is the list of subsets: " + str(subsets_with_duplicates([1, 5, 3, 3])))

main()