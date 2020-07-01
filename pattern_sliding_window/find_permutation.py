def find_permutation(str1, pattern):
    freq_map = {}
    match_length = len(pattern)
    for ch in pattern:
        if ch in freq_map:
            freq_map[ch] += 1
        else:
            freq_map[ch] = 1
    window_start = 0
    window_end = 0
    for window_end in range(len(str1)):
        if str1[window_end] in freq_map and freq_map[str1[window_end]] > 0:
            freq_map[str1[window_end]] -= 1
            match_length -= 1
            if match_length == 0:
                return True
        else:
            if str1[window_start] in freq_map:
                freq_map[str1[window_start]] += 1
                match_length += 1
            window_start += 1
    return False

def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

main()
