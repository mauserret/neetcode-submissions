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
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                dirs = ((1,0),(-1,0),(0,1),(0,-1))
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)
        return islands

