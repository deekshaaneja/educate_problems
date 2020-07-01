def non_repeat_substring(s):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(s)):
        if s[window_end] not in char_index_map:
            char_index_map[s[window_end]] = window_end
            max_length = max(max_length, window_end - window_start + 1)
        else:
            char_index_map[s[window_end]] = window_end
            window_start = window_end
            max_length = max(max_length, window_end - window_start + 1)
    return max_length



def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()