#https://leetcode.com/problems/max-area-of-island/description/
##time complexity: O(number of rows * number of cols)
#space complexity: O(number of rows * number of cols)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n_rows =  len(grid)
        n_cols = len(grid[0])
        for row in range(n_rows):
            for col in range(n_cols):
                max_area = max(max_area, self.dfs(grid, row, col))
        return max_area
    
    def dfs(self, grid, row, col)-> int:
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
            grid[row][col] = 0
            return 1 + self.dfs(grid, row + 1, col) + self.dfs(grid, row -1, col) + self.dfs(grid, row, col + 1) + self.dfs(grid, row, col - 1)
        return 0