class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        def check(x):
            for i in range(n): parent[i] = i
            edges_used = 0
            upgrades_spent = 0
            
            # 1. MUST-include edges
            must_count = 0
            for u, v, s, m in edges:
                if m == 1:
                    if s < x: return False
                    if not union(u, v): # If cycle is formed, Spanning Tree is impossible
                        return False
                    edges_used += 1
                    must_count += 1
            
            # 2. Optional edges (No upgrade needed)
            for u, v, s, m in edges:
                if m == 0 and s >= x:
                    if union(u, v):
                        edges_used += 1
            
            # 3. Optional edges (Needs upgrade)
            for u, v, s, m in edges:
                if m == 0 and s < x and 2 * s >= x:
                    if upgrades_spent < k:
                        if union(u, v):
                            upgrades_spent += 1
                            edges_used += 1
            
            # To be a valid Spanning Tree, we must have exactly n-1 edges
            return edges_used == n - 1

        low, high = 0, 2 * 10**9
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans