

def test(st, k):
    start = 0
    length = 0
    for end in range(len(st)):
        char_end = st[end]
        if abs(ord(st[end]) - ord(st[start])) <= k:
            start = end
            length += 1
    return length

print(test("afcbedg", 2))
print(test("geeksforgeeks", 3))