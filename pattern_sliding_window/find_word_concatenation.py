
def find_word_concatenation(s, words):
    result_indices = []
    window_start = 0
    num_words = len(words)
    for window_end in range(len(s)):
        freq_map = get_frequency(words)
        curr_word = s[window_start : window_end + 1]
        length_curr_word = window_end+1-window_start
        if curr_word in freq_map:
            # freq_map[curr_word] -= 1
            # if freq_map[curr_word] == 0:
            #     freq_map.pop(curr_word)
            curr_index = int(window_start)
            for j in range(len(words)):
                next_word = s[curr_index : curr_index+length_curr_word]
                if next_word in freq_map:
                    freq_map[next_word] -= 1
                    if freq_map[next_word] == 0:
                        freq_map.pop(next_word)
                        if len(freq_map) == 0:
                            result_indices.append(window_start)
                            window_start = window_end + 1
                    curr_index = curr_index+length_curr_word
                else:
                    window_start += window_end + 1
                    break
    return result_indices


def get_frequency(words):
    freq_map = {}
    for word in words:
        if word in freq_map:
            freq_map[word] += 1
        else:
            freq_map[word] = 1
    return freq_map

def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()