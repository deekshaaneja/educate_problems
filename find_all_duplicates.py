def find_all_duplicates(nums):
    i = 0
    out = []
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            out.append(nums[i])
    return out

print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))