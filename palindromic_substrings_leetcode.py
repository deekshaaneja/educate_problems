def countSubstrings(s):
    window_start, window_end = 0, 1
    char_freq = {}
    count = 0
    uniq_elem_array = [0] * len(s)
    while window_start < window_end:
        if window_end == len(s):
            for i in range(window_start, window_end):
                uniq_elem_array[i] = window_end - window_start
            if s[window_start] in char_freq:
                char_freq[s[window_start]].append(window_end - window_start)
            else:
                char_freq[s[window_start]] = [window_end - window_start]
            break
        elif s[window_end] == s[window_start]:
            window_end += 1
        else:
            for i in range(window_start, window_end):
                uniq_elem_array[i] = window_end - window_start
            if s[window_start] in char_freq:
                char_freq[s[window_start]].append(window_end - window_start)
            else:
                char_freq[s[window_start]] = [window_end - window_start]
            window_start = window_end
            window_end += 1
    for ch in char_freq:
        for elem in char_freq[ch]:
            # count += elem * (elem+1) // 2 - elem
            count += elem * (elem+1) // 2
        # for i in range(1, len(uniq_elem_array) - 1):
        #     if if uniq_elem_array[i] == 1 and s[i-1] == s[i+1]:
        #         min_len = min(uniq_elem_array[i-1], uniq_elem_array[i+1])
        #         count += min_len
    for i in range(1, len(uniq_elem_array) - 1):
        num = uniq_elem_array[i]
        if i+num <len(uniq_elem_array) and  s[i-num] == s[i+num]:
            min_len = min(uniq_elem_array[i-num], uniq_elem_array[i+num])
            count += 1
        
    return count

# print(countSubstrings("aabbaa"))
# print(countSubstrings("abc"))
# print(countSubstrings("aba"))
print(countSubstrings("dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"))

