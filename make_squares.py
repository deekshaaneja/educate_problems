def make_squares(arr):
    n = len(arr)
    left = 0 
    right = n-1
    squares = [0 for x in range(n)]
    highestSquareIdx = n-1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare> rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1
    return squares
    


print(make_squares([-3,-2,1,2]))
        
            