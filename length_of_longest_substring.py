def length_of_longest_substring(s, k):
    temp = []
    d = {}
    for stop_point in range(len(s)):
        temp.append(s[stop_point])
        max_repeating_letter_temp = max_repeating_letter(temp)
        remaining_letters = [elem for elem in temp if elem !=max_repeating_letter_temp]
        if len(remaining_letters) <= k:
            d["".join(temp)] = len(temp)
        else:
            while len(remaining_letters) > k:
                max_repeating_letter_temp = max_repeating_letter(temp)
                temp.pop(0)
                remaining_letters = [elem for elem in temp if elem !=max_repeating_letter_temp]
    maxLen = 0
    maxLenWord = None
    for el in d:
        if d[el] > maxLen:
            maxLen = d[el]
            maxLenWord = el
    return maxLen



def max_repeating_letter(ls):
    d = {}
    max_repeating_letter = ls[0]
    max_count = 1
    for elem in ls:
        if elem in d:
            d[elem] += 1
            if d[elem] > max_count:
                max_count = d[elem]
                max_repeating_letter = elem
        else:
            d[elem] = 1
    return max_repeating_letter
    



# print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))