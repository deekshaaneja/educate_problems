def find_duplicate_cycle(nums):
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    curr = nums[nums[slow]]
    cycle_len = 1
    while curr != nums[nums[slow]]:
        curr = nums[curr]
        cycle_len += 1
    
    return find_start(nums, cycle_len)

def find_start(nums, cycle_len):
    pointer1 , pointer2 = nums[0], nums[0]
    while cycle_len >0:
        pointer2 = nums[pointer2]
        cycle_len -= 1
        
    while pointer1 != pointer2:
        pointer1 = nums[pointer1]
        pointer2 = nums[pointer2]
    return pointer1

print(find_duplicate_cycle([2, 1, 3, 3, 5, 4]))


