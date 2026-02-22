from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        # Not enough cables
        if len(connections) < n - 1:
            return -1
        
        graph = defaultdict(list)
        
        # Build graph
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        
        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        components = 0
        
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        
        return components - 1
