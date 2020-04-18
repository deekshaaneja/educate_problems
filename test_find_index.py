def find_switch(s):
    i = 0
    num = s[0]
    while True:

        chunk_s = s[i: 100+i]
        if len(chunk_s)  == 0:
            break
        if chunk_s[-1] != num:
            count = 0
            for elem in chunk_s:
                if elem != num:
                    return i + count
                else:
                    count += 1
        else:
            i += 100
    return -1
s = "a" * 500 + "b" * 50
print(find_switch(s)) 