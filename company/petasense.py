

def longest_inp(start_index, input_str, last_char, k):
    diff = 0
    if start_index == len(input_str):
        return 0

    if last_char is not None:
        diff = abs(ord(input_str[last_char]) - ord(input_str[start_index]))


    left = (1 + longest_inp(start_index+1, input_str, start_index, k)) if diff <= k else 0
    right = longest_inp(start_index+1, input_str, last_char, k) 

    return max(left, right)

print(longest_inp(0, "afcbedg", None, 2))