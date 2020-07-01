


def build_fibnocci_series(max_num):
    ls = [0, 1]
    for num in range(2, max_num + 1):
        fib_num = ls[-2] + ls[-1]
        ls.append(fib_num)
    return ls


print(build_fibnocci_series(10))