def pair_with_targetsum(arr, target_sum):
    nums = {}
    for i,num in enumerate(arr):
        if target_sum - num in nums:
            return nums[target_sum-num],i
        else:
            nums[arr[i]] = i

print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
