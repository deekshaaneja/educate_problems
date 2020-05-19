

with open("exclude.txt") as f:
    stopwords = f.readlines()
    stopwords_set = set(stopwords.split(","))

freq_map = {}
min_heap = []
added_words = set()
def find_most_used_words(text_article):
    text_arr = text_article.split()
    for word in text_arr:
        if word not in stopwords_set:
            if word in freq_map:
                freq_map[word] += 1
            else:
                freq_map[word] = 1
    elem_count_tup = [(k,v) for k,v in freq_map.items()]
    elem_count_tup_sorted = elem_count_tup.sort(lambda  value: value[1], desc)
    return elem_count_tup_sorted
    # return freq_map


