#https://leetcode.com/problems/is-graph-bipartite/description/
#time complexity: O(n+e) where n is the number of nodes of the undirected graph
#space complexity: O(n) where n is the number of nodes of the unidrected graph
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        for node_index in range(len(graph)):
            if colors[node_index] == 0 and not self.dfs(graph, colors, node_index, 1):
                return False
        return True
        
    def dfs(self,graph, colors, node_index, curr_color):
            colors[node_index] = curr_color
            for neighbor in graph[node_index]:
                if colors[neighbor] == 0 and not self.dfs(graph, colors, neighbor, -curr_color):
                    return False
                elif colors[neighbor] == colors[node_index]:
                    return False
            return True
        