# prev 
# curr
# min_count_of_arrows
# [5, 5, 5]
# {}
# curr = arr[0]

# s = ""

def find_min_arrows(arr_height):
    min_count_of_arrows = 1
    previous = 0
    current = 0
    arrow_map = {}
    for current in range(1, len(arr_height)):
        print(arrow_map)
        if arr_height[previous] - arr_height[current] == 1:
            previous = current
        else:
            if arr_height[current] not in arrow_map:
                min_count_of_arrows += 1
            else:
                if arrow_map[arr_height[current] - 1] in arrow_map:
                    arrow_map[arr_height[current] - 1] += 1
                else:
                    arrow_map[arr_height[current] - 1] = 1
                arrow_map[arr_height[current]] - 1
            # if arr_height[current] - 1 > 0:
            #     if arr_height[current] - 1 in arrow_map:
            #         arrow_map[arr_height[current] - 1] += 1
            #     else:
            #         arrow_map[arr_height[current] - 1] = 1
    return min_count_of_arrows, arrow_map

# {4:[1]}

# print(find_min_arrows([6, 5, 1, 4, 5]))
# print(find_min_arrows([5, 5, 5]))
# print(find_min_arrows([7, 5, 6, 4, 3]))
print(find_min_arrows([7, 5, 6, 3, 4, 1]))

# {6: 1, 4: [], 5:[]}

# arr[curr] -1
# arr[curr]
# { 5: [3]}
