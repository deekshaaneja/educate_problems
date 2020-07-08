'''    Input: arr[] = {5, 10, 12, 13, 15, 18, 14}, K = 30,k = 20
    Output: {12, 18}, {5, 12, 13}, {5, 10, 15}'''

# set()
# iterate arr, target_elem

def find_pairs(arr, k):
    currSum = arr[0]
    start_ptr = 0
    end_ptr = 0
    result = []
    while end_ptr < len(arr):
        if currSum == k:
            result.append(arr[start_ptr : end_ptr + 1])

        if currSum <= k:
            end_ptr += 1
            if end_ptr < len(arr):
                currSum = currSum + arr[end_ptr]

        else:
            currSum -= arr[start_ptr]
            start_ptr += 1
    return result
    


def find_target_array(arr, k):
    arr.sort()
    window_start = 0
    currentSum = 0
    result = []
    for window_end in range(len(arr)):
        currentSum += arr[window_end]
        if currentSum == k:
            result.append(arr[window_start:window_end+1])
        elif currentSum > k:
            while window_start != window_end:
                currentSum -= arr[window_start]
                window_start += 1
                if currentSum == k:
                    result.append(arr[window_start:window_end+1])
    return result

# def find_pair_sum(ls, target):
#     set_ls = set()
#     for i in range(len(ls)):
#         target_elem = target - ls[i]
#         if target_elem in 


# def find_target_sum_2(arr, k):
#     set_st = set()
#     result = []
#     for i in range(len(arr)):
#         if arr[i] == k:
#             result.append([arr[i]])
#         target_num = k - arr[i]
#         if target_num in set_st:
#             result.append(arr[i], target_num)
#         else:
#             for elem in set_st:



def main():
    print(find_pairs([5, 10, 12, 13, 15, 18, 14], 30))

main()
