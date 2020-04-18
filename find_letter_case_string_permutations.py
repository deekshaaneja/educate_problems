def find_letter_case_string_permutations(word):
    word_list = list(word)
    sublist = []
    sublist.append(word_list)
    for i in range(len(word_list)):
        n = len(sublist[i])
        for j in range(n):
            new_elem = list(sublist[j])
            if new_elem[j].isalpha() == True:
                new_elem[j] = new_elem[j].swapcase()
                sublist.append(new_elem)
    permutations = ["".join(x) for x in sublist]
    return permutations

def main():
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()

        