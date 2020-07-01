def search_next_letter(letters, key):
    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if ord(letters[mid]) == ord(key):
            return letters[mid+1]
        elif ord(key) > ord(letters[mid]):
            left = mid + 1
        elif ord(key) < ord(letters[mid]):
            right = mid -1
    return letters[left % len(letters)]

def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
