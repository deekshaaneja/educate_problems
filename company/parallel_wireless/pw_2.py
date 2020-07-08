# a = "yycbe"
# b = "yceyb"

# b = yyecb
# b = yyceb
# b = yycbe 3 iterations

# a = "yycbe"
# b = "yceyz"


def convert(a, b):
    freq_map = {}
    res = ""
    for i in range(len(a)):
        if a[i] in freq_map:
            freq_map[a[i]] += 1
        else:
            freq_map[a[i]] = 1
    for j in range(len(b)):
        if b[j] in freq_map:
            freq_map[b[j]] -= 1
            if freq_map[b[j]] == 0:
                freq_map.pop(b[j])
        else:
            res = -1
    if len(freq_map) == 0:
        counter = 0
        b_list = list(b)
        for i in range(len(b_list)):
            if b_list[i] != a[i]:
                j = i
                while b_list[j] != a[i]:
                    j += 1
                b_list[i] , b_list[j] = b_list[j], b_list[i]
                counter += 1
        res = ("".join(b_list), counter)
    print(res)


def main():
    a = "yycbe"
    b = "yceyb"
    convert(a, b)
    c = "yycbe"
    d = "yceyz"
    convert(c, d)
    e = "aacbef"
    f = "acefab"
    convert(e, f)
    g = "aacbejf"
    h = "acefabj"
    convert(g, h)


main()
