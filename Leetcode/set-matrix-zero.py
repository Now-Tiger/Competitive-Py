'''
Problem  : Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, 
           and return the matrix.You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''

def setzeros(matrix) :
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()
    
    # Marking those rows & cols which we want to be made zeros :
    for i in range(R) :
        for j in range(C) :
            if matrix[i][j] == 0 :
                rows.add(i)
                cols.add(j)
    
    # Iterate once again through entire array :
    for i in range(R) :
        for j in range(C) :
            if i in rows or j in cols :
                matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setzeros(matrix)
matrix


