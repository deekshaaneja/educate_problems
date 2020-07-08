def find_subsets(arr):
    res = []
    res.append([])
    for i in range(len(arr)):
        for j in range(len(res)):
            elem = res[j] + [arr[i]]
            res.append(elem)
    return res

def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

