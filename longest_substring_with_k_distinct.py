def longest_substring_with_k_distinct(s, k):
    
    window_start = 0
    distinct_chars = {}
    maxLen = 0
    for window_end in range(len(s)):
        if s[window_end] in distinct_chars:
            distinct_chars[s[window_end]] += 1
        else:
            distinct_chars[s[window_end]] = 1
        if len(distinct_chars) > k:
            distinct_chars[s[window_start]] -= 1
            if distinct_chars[s[window_start]] == 0:
                distinct_chars.pop(s[window_start], None)
            window_start += 1
        maxLen = max(maxLen, len(s[window_start: window_end+1]))
    return maxLen
            

def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
