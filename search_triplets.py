def search_triplets(arr):
    arr.sort()
    triplet_set = set()
    for i in range(len(arr)):
        num = arr[i]
        j = i+1
        pair = search_pair(j, num, arr)
        if pair is not None:
            triplet_set.add((num,pair[0],pair[1]))
    return triplet_set

def search_pair(index, num, arr):
    d = {}
    for j in range(index, len(arr),1):
        target = -num-arr[j]
        if target in d:
            return arr[j], target
        else:
            d[arr[j]] = j
    return None

print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
