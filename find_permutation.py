def find_permutation(input_str, pattern):
    window_start = 0
    d = {}
    for el in pattern:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    for window_end in range(len(input_str)):
        matched = 0
        window = input_str[window_start: window_end+1]
        for el in window:
            if el in d:
                matched += 1
                if matched == len(d):
                    return True
                elif len(window) > len(d):
                    if input_str[window_start] not in d:
                        window_start += 1
                    else:
                        matched -= 1
                        window_start += 1
                else:
                    window_end += 1
            else:
                window_end += 1
    return False

def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()

            

def find_permutations_of_string(s, i, length):
    if i == length:
        return " ". join(s)
    else:
        for j in range(i, length):
            s[i], s[j] = s[j], s[i]
            find_permutations_of_string(s, i + 1, length)
            s[i], s[j] = s[j], s[i]
