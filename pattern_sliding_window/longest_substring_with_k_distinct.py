def longest_substring_with_k_distinct(s, k):
    window_start = 0
    frequency_map = {}
    max_len = 0
    longest_substring = None
    for window_end in range(len(s)):
        current_string = s[window_start:window_end]
        current_string_len = find_distinct_chars(current_string)
        if current_string_len <= k:
            frequency_map[current_string] = current_string_len
        else:
            window_start += 1
    for elem in frequency_map:
        if frequency_map[elem] > max_len:
            longest_substring = elem
    return longest_substring


def find_distinct_chars(substring):
    sub_set = set(substring)
    return len(sub_set)

def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("aabacbebebe", 3)))


main()
