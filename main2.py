def invers(arr):
    reverse = [row[::-1] for row in arr]
    inverted = [[1 - cell for cell in row] for row in reverse]
    return inverted
        
        
arr = [[0,1,0],
       [0,1,1],
       [1,0,0]]


matrix = invers(arr)
for row in matrix:
    print(row)