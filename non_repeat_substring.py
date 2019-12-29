def non_repeat_substring(s):
    window_start = 0
    max_chars = {}
    max_substring = 0
    for window_end in range(len(s)):
        if s[window_end] not in max_chars:
            max_chars[s[window_end]] = 1
        else:
            max_chars = {s[window_end-1]:1}
            window_start += 1
        max_substring = max(max_substring, len(max_chars))
    return max_substring

def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()