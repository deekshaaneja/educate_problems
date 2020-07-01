def longest_substring_with_k_distinct(s, k):
    window_start = 0
    max_len = 0
    freq_map = {}
    curr_len = 0
    for window_end in range(len(s)):
        if s[window_end] in freq_map:
            freq_map[s[window_end]] += 1
        else:
            freq_map[s[window_end]] = 1
        curr_len += 1
        if len(freq_map) > k:
            freq_map[s[window_start]] -= 1
            if freq_map[s[window_start]] == 0:
                freq_map.pop(s[window_start])
            window_start += 1
            curr_len -= 1
        max_len = max(curr_len, max_len)
    return max_len



def find_distinct_chars(substring):
    sub_set = set(substring)
    return len(sub_set)

def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("aabacbebebe", 3)))


main()
