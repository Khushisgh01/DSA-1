from collections import deque

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [0] * n
        
        for i in range(n):
            if color[i] != 0:
                continue
            
            queue = deque([i])
            color[i] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        
        return True
