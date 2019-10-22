def cyclic_sort(nums):
    for i in range(len(nums)):
        if nums[i] - 1 == i:
            i = i + 1
        else:
            while nums[i] - 1 != i:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
    return nums

# print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))