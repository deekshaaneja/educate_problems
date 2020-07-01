def find_key(dict_input, k):
    if k in dict_input:
        return dict_input[k]
    else:
        return 0

print(find_key({"a": 1, "b":2}, "a"))