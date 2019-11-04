def find_string_anagrams(s, pattern):
    d = {}
    window_start = 0
    ls = []
    match = 0
    for el in pattern:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    result_indices = []
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in d:
            d[right_char] -= 1
            if d[right_char] == 0:
                match += 1
        if match == len(d):
            result_indices.append(window_start)
        
        if window_end >= len(pattern) - 1:
            left_char = s[window_start]
            window_start += 1
            if left_char in d:
                if d[left_char] == 0:
                    match -= 1
                d[left_char] += 1
    return result_indices

def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()


