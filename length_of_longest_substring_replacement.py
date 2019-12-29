def length_of_longest_substring_replacement(s, k):
    count_chars = {}
    window_start = 0
    max_count = 0
    for window_end in range(len(s)):
        if s[window_end] in count_chars:
            count_chars[s[window_end]] += 1
            max_count = max(max_count, count_chars[s[window_end]])
            if max_count == count_chars[s[window_end]]:
                max_count_char = s[window_end]
        else:
            count_chars[s[window_end]] = 1
        if 
    return max_count_char

def main():
    print(length_of_longest_substring_replacement("aabccbb", 2))
    print(length_of_longest_substring_replacement("abbcb", 1))
    print(length_of_longest_substring_replacement("abccde", 1))


main()
