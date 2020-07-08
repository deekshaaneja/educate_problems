# arr = [1, 2, 2, 3, 4, 4, 5]

# j = 1, i =2
# j =2, i = 2
# i = 3, 

def remove_dup(arr):
    j = 1
    for i in range(len(arr)):
        if arr[i] != arr[j-1]:
            print(arr[i], arr[j])
            if i - j > 1:
                arr[j+1] = arr[i]
            j += 1
    return arr[:j]

def main():
    print(remove_dup([1, 2, 2, 3, 4, 4, 5]))

main()
