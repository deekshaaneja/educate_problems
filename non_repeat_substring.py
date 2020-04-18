def non_repeat_substring(s):
    window_start =0
    window_end = 1
    frequency_map = {}
    max_length = 0
    for window_end in range(len(s)):
        word = s[window_start : window_end]
        if s[window_end] in frequency_map:
            frequency_map[s[window_end]] += 1
        else:
            frequency_map[s[window_end]] = 1
        if count_chars(frequency_map) == True:
            current_max = len(frequency_map)
            if current_max > max_length:
                max_length = current_max
        else:
            frequency_map[s[window_start]] -= 1
            if frequency_map[s[window_start]] == 0:
                frequency_map.pop(s[window_start])
            window_start += 1
    return max_length
        

def count_chars(d):
    for char in d:
        if d[char] > 1:
            return False
    return True 


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()