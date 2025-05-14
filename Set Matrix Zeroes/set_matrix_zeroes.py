''''
https://leetcode.com/problems/set-matrix-zeroes/
time complexity: O(row_len * col_len )
space complexity: O(1)
approach:
Use the first row and first column of the matrix itself as marker storage:
If a cell matrix[i][j] is 0, mark:
        matrix[0][j] = 0 (column marker)
        matrix[i][0] = 0 (row marker)
Special care is needed for the first column, since it overlaps with matrix[0][0]. So we use a separate variable: col_zero.

'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_zero = 1 #this variable is marker to tell us if the 1st column is to be zero
        row_len = len(matrix)
        col_len = len(matrix[0])
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    if j == 0:
                        col_zero = 0
                    else:
                        matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,row_len): #setting matrix cells those in 0th column and 0th row to zeroes
            for j in range(1,col_len):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0: #setting column markers to zeroes
            for i in range(col_len):
                matrix[0][i] = 0

        if col_zero == 0: #setting row markers to zeroes
            for i in range(row_len):
                matrix[i][0] = 0
'''
If you zero the first column first, and then check matrix[0][0], its value may have been overwritten (to 0) as part of the first column update.
This would falsely trigger the zeroing of the first row even if it shouldn’t be zeroed.
'''

        
        
        
