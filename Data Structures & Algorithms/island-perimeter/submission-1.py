class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        tot = [0]
        def dfs(row, col):
            if (row, col) in visited: return
            visited.add((row, col))
            if (row + 1 < ROWS and grid[row + 1][col] != 0): dfs(row + 1, col) 
            else: tot[0] += 1
            if (row - 1 > -1 and grid[row - 1][col] != 0): dfs(row - 1, col) 
            else: tot[0] += 1
            if (col + 1 < COLS and grid[row][col + 1] != 0): dfs(row, col + 1) 
            else: tot[0] += 1
            if (col - 1 > -1 and grid[row][col - 1] != 0): dfs(row, col - 1) 
            else: tot[0] += 1
            return 


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col)
        return tot[0]
            