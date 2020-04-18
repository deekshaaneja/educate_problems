def find_water(arr):
    left_arr = [0] * len(arr)
    right_arr = [0] * len(arr)

    amount = 0
    left_arr[0] = arr[0]
    for i in range(1, len(arr)):
        left_arr[i] = max(left_arr[i-1], arr[i])
        
    right_arr[ len(arr) - 1] = arr[len(arr) - 1]
    for j in range(len(arr) -2, -1, -1):
        right_arr[j] = max(right_arr[j+1], arr[j])
        
    for k in range(len(arr)):
        amount += min(left_arr[k], right_arr[k]) - arr[k]

    return amount
    
print(find_water([8, 1, 2, 4, 6, 8, 5, 7, 4, 2, 3]))
# print(find_water([7, 5, 7, 4]))