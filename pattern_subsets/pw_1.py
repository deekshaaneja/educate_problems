def is_anagram(st1, st2):
    if len(st1) != len(st2):
        return False
    ls = [elem for elem in st2 if elem not in st1]
    if len(ls) == 0:
        return True
    return False

def is_anagram_map(st1, st2):
    if len(st1) != len(st2):
        return False
    freq_map = {}
    for elem in st1:
        if elem in freq_map:
            freq_map[elem] += 1
        else:
            freq_map[elem] = 1
    for elem in st2:
        if elem in freq_map:
            freq_map[elem] -= 1
            if freq_map[elem] == 0:
                freq_map.pop(elem)
        else:
            return False
        if len(freq_map) == 0:
            return True


def main():
    print(is_anagram("abc", "bac"))
    print(is_anagram_map("abc", "bac"))
    print(is_anagram("ac", "bac"))
    print(is_anagram_map("ac", "bac"))


main()