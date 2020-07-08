# Input: [2, 3, 3, 3, 6, 9, 9]


def remove_duplicates(arr):
    j = 0
    i = 1
    count = 0
    while i < len(arr):
        if arr[i] != arr[j]:
            j += 1
            i += 1
        else:
            while i < len(arr) and arr[i] == arr[j]:
                i += 1
                count += 1
            while i < len(arr) and count != 0:
                arr[j+1] = arr[i]
                j += 1
                i += 1
                count -= 1
    return arr[:j+1]

def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
            


        