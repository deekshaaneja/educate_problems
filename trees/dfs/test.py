



def bin_search(ls, k):
    a = 0 #0
    b = len(ls) - 1 #5
    mid = a + (b-a)//2

    while a <= b:
        if ls[mid] == k:
            return mid
        elif ls[mid] < k:
            a = mid + 1
        else:
            b = mid -1
        if a == b - 1:
            break
    return None


# print(bin_search([1, 2, 3, 4, 5], 3))
# print(bin_search([1, 2, 3, 4, 5], 6))
# print(bin_search([1, 2, 3, 4, 5], 0))
# print(bin_search([1, 2, 4, 5], 3))


# ls = [3, 4, 5, 1, 2]
# 2, 3, 4, 5, 1
# 5, 1, 2, 3, 4

def find_min_element(ls):
    a = 0
    b = len(ls) -1
    mid = a + (b-a) //2
    while a < b:
        if ls[mid-1] > ls[mid]:
            return mid
        elif ls[mid + 1] < ls[mid]:
            return mid+1
        elif ls[mid] > ls[mid-1]:
            b = mid -1
        else:
            a = mid + 1
        if a == b - 1:
            break
    return -1


print(find_min_element([3, 4, 5, 1, 2]))
print(find_min_element([3, 4, 5, 6, 7, 1, 2]))


        
    
