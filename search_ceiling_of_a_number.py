def search_ceiling_of_a_number(arr, key):
    if len(arr) == 1:
        if key < arr[0]:
            return arr[0]
        else:
            return None
    if len(arr) % 2 == 0:
        midpoint = int(len(arr)/2)
    else:
        midpoint = int((len(arr) + 1) / 2) - 1
    if key == arr[midpoint]:
        return arr[midpoint]
    elif key > arr[midpoint]:
        ls = arr[midpoint:]
        return search_ceiling_of_a_number(ls, key)
    elif key < arr[midpoint]:
        if key > arr[midpoint-1]:
            ls = arr[midpoint:]
            return search_ceiling_of_a_number(ls, key)
        else:
            ls = arr[:midpoint]
            return search_ceiling_of_a_number(ls, key)

def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()