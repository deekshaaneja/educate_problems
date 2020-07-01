
# arr = [4,3,2,3,5,2,1]
arr = [2,3,4,1]
target = 5


def hasSum(arr, index, sum, targetSum):

    if index == len(arr):
        if sum == 0 or sum == targetSum:
            return True
        else:
            return False

    val = arr[index]

    if val > targetSum:
        return False

    if val == sum:
        if (hasSum(arr, index+1, sum, targetSum)) == False:
            return False
    else:
        if (hasSum(arr, index+1, sum-val, targetSum)) == False:
            return False
    
    return True




print(hasSum(arr, 0, target, target))