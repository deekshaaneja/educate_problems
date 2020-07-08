def search_in_infinite_array(arr, key):
    idx = 0
    current_idx = 2**idx
    while True:
        previous_idx = current_idx
        current_idx = 2**idx
        if current_idx < len(arr):
            if arr[current_idx] == key:
                return current_idx
            elif key > arr[current_idx]:
                idx += 1
            elif key>arr[previous_idx] and key < arr[current_idx]:
                value = search_in_infinite_array(arr[previous_idx: current_idx+1], key)
                return previous_idx + value if value != -1 else -1 
            else:
                return -1
        else:
            return -1
    return -1

def main():
    reader = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = [1, 3, 8, 10, 15]
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()