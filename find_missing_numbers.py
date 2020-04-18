def find_missing_numbers(nums):
    i = 0
    result = []
    while True:
        if i == len(nums):
            break
        if nums[i] != i + 1:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
    for k in range(1, len(nums)):
        if k != nums[k-1]:
            result.append(k)
    return result


print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))