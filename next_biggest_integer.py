def next_biggest_integer(num):
    ls = list(str(num))
    for i in range(len(ls)-1, -1, -1):
        j = i-1
        ls[i], ls[j] = ls[j], ls[i]
        new_num = int("".join(ls))
        if new_num > num:
            return new_num

print(next_biggest_integer(1469))        

