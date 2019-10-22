def find_missing_number(nums):
    i = 0
    for i in range(len(nums)):
        if nums[i]  == i:
            i += 1
        else:
            while nums[i] != i and nums[i] < len(nums):
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return nums

print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))