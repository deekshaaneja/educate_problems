


def fib(n, dp_arr):
    if n < len(dp_arr):
        return dp_arr[n]
    if n == 0 or n == 1:
        return n
    return fib(n - 1, dp_arr) + fib(n-2, dp_arr)


def test():
    k = 5000000
    dp_arr = []
    for i in range(k):
        v = fib(i, dp_arr)
        dp_arr.append(v)
        if v == k:
            return True
        if v > k:
            return False
    return False

print(test())