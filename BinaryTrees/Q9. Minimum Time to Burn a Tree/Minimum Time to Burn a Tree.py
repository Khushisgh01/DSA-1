from collections import deque

class Solution:
    def minTime(self, root, target):
        
        # Step 1: Create parent mapping
        parent = {}
        target_node = None
        
        def dfs(node, par):
            nonlocal target_node
            if not node:
                return
            
            if node.data == target:
                target_node = node
            
            parent[node] = par
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        # Step 2: BFS from target node
        queue = deque([target_node])
        visited = set([target_node])
        
        time = -1
        
        while queue:
            size = len(queue)
            time += 1
            
            for _ in range(size):
                node = queue.popleft()
                
                # Check all 3 directions
                for neighbor in (node.left, node.right, parent[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return time
