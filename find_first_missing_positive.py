def find_first_missing_positive(nums):
    i = 0
    while i < len(nums):
        j = nums[i] -1
        # if j< len(nums):
        if nums[i]>0 and nums[i] <= len(nums) and nums[i] != nums[j] :
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if i != nums[i] - 1:
            return i+1

def find_first_missing_positive1(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return nums.length + 1


# print(find_first_missing_positive([-3, 1, 5, 4, 2]))
print(find_first_missing_positive([3, 2, 5, 1]))
