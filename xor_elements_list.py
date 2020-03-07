'''Find the element that appears once in an array where every other element appears twice'''

def find_single_element(ls):
    xor_result = ls[0]
    for i in range(1, len(ls)):
        xor_result = xor_result ^ ls[i]
    return xor_result

print(find_single_element([7, 3, 5, 4, 5, 3, 4]))