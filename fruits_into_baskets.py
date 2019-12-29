def fruits_into_baskets(fruits):
    fruit_count = {}
    window_start = 0
    max_fruits = 0
    curr_fruits = 0
    for window_end in range(len(fruits)):
        if fruits[window_end] not in fruit_count:
            fruit_count[fruits[window_end]] = 1
            curr_fruits += 1
        else:
            fruit_count[fruits[window_end]] += 1
            curr_fruits += 1
        if len(fruit_count) > 2:
            fruit_count[fruits[window_start]] -= 1
            curr_fruits -= 1
            if fruit_count[fruits[window_start]] == 0:
                fruit_count.pop(fruits[window_start])
            window_start += 1
        max_fruits = max(max_fruits, curr_fruits)
    return max_fruits

def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()