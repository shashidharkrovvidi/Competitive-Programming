#https://leetcode.com/problems/rotting-oranges/description/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_fresh = 0
        minutes = 0
        n_rows = len(grid)
        n_cols = len(grid[0])
        queue = deque()
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    n_fresh += 1
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue and n_fresh>0:
            minutes += 1
            queue_size = len(queue)
            for _ in range(queue_size):
                row, col = queue.popleft()
                for dir in dirs:
                    row_next = dir[0] + row
                    col_next = dir[1] + col
                    if 0 <= row_next < n_rows and 0 <=col_next < n_cols and grid[row_next][col_next] == 1:
                        grid[row_next][col_next] = 2
                        queue.append((row_next, col_next))
                        n_fresh -= 1
        return minutes if n_fresh == 0 else -1

        