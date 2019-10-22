def find_first_k_missing_positive(nums, k):
    i = 0
    out = []
    count = 0
    n = len(nums)
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <=len(nums) and  nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            out.append(i + 1)
            i += 1
            count += 1
        if i == len(nums) - 1:
            out += list(range(max(nums)+1, k-count+max(nums)+1))
            count = k
        if count == k:
            break
    return out

def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()