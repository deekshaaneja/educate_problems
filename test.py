import math

def int_to_binary(num):
    quo = num
    ls = []
    while num != 2 :
        rem = num % 2
        num = num // 2
        ls.append(str(rem))
    if num == 2:
        ls.append(str(10))
    output = ls.reverse()
    return "".join(ls)

print(int_to_binary(42))