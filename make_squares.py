def make_squares(arr):
    squares = [n *n for n in arr]
    n = len(arr)
    highest_square_index = n -1
    left, right = 0, n-1
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1
        highest_square_index -= 1
    return squares

def find_non_negative_index(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            return i
    return None
    


print(make_squares([-3,-2,1,2]))
        
            