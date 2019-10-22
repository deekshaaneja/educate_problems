def non_repeat_substring(s):
    ls = list(s)
    temp = []
    dict_temp = {}
    for i in range(len(s)):
        temp.append(ls[i])
        if len(temp) == len(set(temp)):
            dict_temp["".join(temp)] = len(set(temp))
        while len(temp) != len(set(temp)):
            temp.pop(0)
            if len(temp) == len(set(temp)):
                dict_temp["".join(temp)] = len(set(temp))
    maxVal = 1
    for elem in dict_temp:
        if dict_temp[elem] > maxVal:
            maxVal = dict_temp[elem]
            max_substring = elem
    return max_substring, maxVal

print(non_repeat_substring("aabccbzxvb"))