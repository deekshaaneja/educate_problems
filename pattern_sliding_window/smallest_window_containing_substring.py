
def find_substring(st, pattern):
    window_start = 0
    freq_map = {}
    word_tup = []
    for window_end in range(len(st)):
        current_word = st[window_start : window_end + 1]
        if st[window_end] in pattern:
            if st[window_end] in freq_map:
                freq_map[st[window_end]] += 1
            else:
                freq_map[st[window_end]] = 1
            while is_pattern_exist(freq_map, pattern):
                word_tup.append((st[window_start : window_end + 1], window_end - window_start + 1))
                if st[window_start] in pattern:
                    freq_map[st[window_start]] -= 1
                    if freq_map[st[window_start]] == 0:
                        freq_map.pop(st[window_start])
                window_start += 1
    if len(word_tup) == 0:
        return ''
    shortest_word = min(word_tup, key=lambda item:item[1])
    return shortest_word[0]


def is_pattern_exist(freq_map, pattern):
    for character in pattern:
        if character in freq_map and pattern.count(character) <= freq_map[character]:
            continue
        else:
            return False
    return True

def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdabca", "abc"))
    print(find_substring("adcad", "abc"))

main()