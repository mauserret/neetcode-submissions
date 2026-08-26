class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
                if r > 0:
                    dfs(r - 1, c)
                if r < rows - 1:
                    dfs(r + 1, c)
                if c > 0:
                    dfs(r, c - 1)
                if c < cols - 1:
                    dfs(r, c + 1)

        tot = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    tot += 1
                    dfs(r, c)
        return tot
        """
        rows, cols = len(grid), len(grid[0])
        tot = 0
        visit = set()
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    tot += 1 
        return tot
