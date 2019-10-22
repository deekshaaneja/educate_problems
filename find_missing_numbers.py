def find_missing_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    out = []
    for i in range(len(nums)):
        if i != nums[i] -1:
            out.append(i)
    return out
print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))