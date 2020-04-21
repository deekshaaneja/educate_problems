def cyclic_sort(nums):
    for i in range(len(nums)):
        if nums[i] != i+1:
            while nums[i] != i+1:
                swap_index = nums[i] -1
                nums[i], nums[swap_index] = nums[swap_index], nums[i]
    return nums

print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))