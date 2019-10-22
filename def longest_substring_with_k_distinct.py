def longest_substring_with_k_distinct(s, k):
    distinct_char_dict = {}
    ls = list(s)
    ls_temp = []
    for i in range(len(ls)):
        ls_temp.append(ls[i])
        distinct_char_count = len(set(ls_temp))
        if distinct_char_count <= k:
            distinct_char_dict["".join(ls_temp)] = distinct_char_count
        else:
            # distinct_char_count = len(set(ls_temp))
            while distinct_char_count > k:
                ls_temp.pop(0)
                distinct_char_count = len(set(ls_temp))
            distinct_char_dict["".join(ls_temp)] = distinct_char_count
    maxElem = 1
    for elem in distinct_char_dict:
        if len(elem) > maxElem:
            maxElem = len(elem)
    return maxElem

print(longest_substring_with_k_distinct("cbbebi", 3))
print(longest_substring_with_k_distinct("araaci", 1))


