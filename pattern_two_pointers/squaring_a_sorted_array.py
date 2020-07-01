import math

def make_squares(arr):
    squares = [0] * len(arr)
    first_pos_idx = 0
    j = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            first_pos_idx = i-1
            break
    for j in range(len(squares)):
        if first_pos_idx >= 0 and i < len(arr):
            if abs(arr[first_pos_idx]) < abs(arr[i]):
                squares[j] = arr[first_pos_idx] * arr[first_pos_idx]
                first_pos_idx -= 1
            else:
                squares[j] = arr[i] * arr[i]
                i += 1
    print(i, first_pos_idx)
    if first_pos_idx >= 0 and j <= len(squares) - 1:
        while first_pos_idx >= 0:
            squares[j] = arr[first_pos_idx] * arr[first_pos_idx]
            j += 1
            first_pos_idx -= 1
    if i <= len(arr) - 1 and j <= len(squares) - 1:
        while i <= len(arr) - 1:
            squares[j] = arr[i] * arr[i]
            j += 1
            i += 1
    return squares
    

def main():

    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()

