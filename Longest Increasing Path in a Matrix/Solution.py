#https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#time complexity: o(m*n) where m is the number of rows and n is the number of columns of a matrix
#space complexity: O(m*n) ; m* n  would be the worst case size of the recursion stack and the size of the memo table as well
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        max_len = 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                max_len = max(max_len,self.dfs(matrix, row, col, memo))
        return max_len

    def dfs(self,matrix, row, col, memo):
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        if memo[row][col] != 0:
            return memo[row][col]
        max_len = 1
        for dir in dirs:
            row_next = dir[0] + row
            col_next = dir[1] + col
            if 0 <= row_next < len(matrix) and 0 <= col_next < len(matrix[0]) and matrix[row_next][col_next] > matrix[row][col]:
                max_len = max(max_len, 1 + self.dfs(matrix, row_next, col_next, memo))
        memo[row][col] = max_len
        return max_len
        
        
        