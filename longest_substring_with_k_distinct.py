def longest_substring_with_k_distinct(s, k):
    frequency_map = {}
    max_length = 0
    start, end = 0, 1
    while end <= len(s) - 1:
        word = s[start: end]
        if s[end - 1] in frequency_map:
            frequency_map[s[end - 1]] += 1
        else:
            frequency_map[s[end - 1]] = 1
        if len(frequency_map) <= k:
            count = get_value_sum(frequency_map)
            if count > max_length:
                max_length = count
        elif len(frequency_map) > k:
            frequency_map[s[start]] -= 1
            if frequency_map[s[start]] == 0:
                frequency_map.pop(s[start])
            start += 1
        end = end + 1
            
    return max_length

def get_value_sum(d):
    count = 0
    for character in d:
        count += d[character]
    return count

        



            

def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
