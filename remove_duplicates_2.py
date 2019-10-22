def remove_duplicates(arr):
    length_unique_nums = 0
    last_num = None
    for num in arr:
        if num != last_num:
            length_unique_nums +=1
        last_num = num

    return length_unique_nums

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))