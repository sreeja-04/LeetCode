class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)        
        color = [-1] * V

        def dfs(i, c):
            color[i] = c
            for nei in graph[i]:
                if color[nei] == -1:
                    if not dfs(nei, 1-c):
                        return False
                elif color[nei] == c:
                    return False
            return True

        for i in range(V):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
                
            
        return True

