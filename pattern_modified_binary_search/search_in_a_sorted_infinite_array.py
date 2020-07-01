def search_in_infinite_array(arr, key):
    curr = 0
    index = 2**curr
    if len(arr) < 1:
        return -1
    while True:
        prev = index
        index = 2**curr
        # print(index)
        if index > len(arr) - 1:
            return -1
        if arr[index] == key:
            return index
        elif key > arr[index]:
            curr += 1
        elif key < arr[index]:
            res = search_in_infinite_array(arr[prev:index], key)
            return prev + search_in_infinite_array(arr[prev:index], key) if res != -1 else -1
    return -1

def main():
    reader = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = [1, 3, 8, 10, 15]
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
