from collections import deque

def find_permutations(nums):
    result = []
    nums_length = len(nums)
    permutations = deque()
    permutations.append([])
    for i in range(nums_length):
        n = len(permutations)
        for j in range(n):
            old_permutations = permutations.popleft()
            for j in range(len(old_permutations) + 1):
                new_permutation = list(old_permutations)
                new_permutation.insert(j, nums[i])
                permutations.append(new_permutation)
                if len(new_permutation) == nums_length:
                    result.append(new_permutation)
    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))

main()