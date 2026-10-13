class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visited = [False] * n
        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)
        return count
