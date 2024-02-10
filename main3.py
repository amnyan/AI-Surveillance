def count_obj(matrix):
    def check(row, col):
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == 1:
            matrix[row][col] = 0
            
            check(row, col + 1)  
            check(row, col - 1) 
            check(row + 1, col) 
            check(row - 1, col)

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                check(i, j)
                count += 1

    return count

matrix = [
    [1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0]
]
print("Count of objects:", count_obj(matrix))