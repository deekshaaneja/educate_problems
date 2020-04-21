def non_repeat_substring(s):
    window_start = 0
    index_map = {}
    max_len_non_repeating = 0
    for window_end in range(len(s)):
        if s[window_end] in index_map:
            index_dup = index_map[s[window_end]][-1]
            if window_start <= index_dup:
                window_start += index_dup + 1
            index_map[s[window_end]].append(window_end)
        else:
            index_map[s[window_end]] = [window_end]
        current_length = window_end - window_start + 1
        max_len_non_repeating = max(current_length, max_len_non_repeating)
    return max_len_non_repeating


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()