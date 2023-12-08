# Shortest Path Algorithm Implementation
"""
n = number of vertices in the graph
edges = a list of tuples, each representing a directed edge in the form (u,v,w) where,
- u is the source vertex
- v is the destination vertex
- w is the weight of the edge
Each vertex is labeled from 0 to n-1
src = source vertex from which to start the algorithm
if a vertex is unreachable from the source vertex, the shortest path distance for the unreachable vertex should be -1
"""

from typing import List, Dict
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int,int]:
        adj={}
        for i in range(n):
            adj[i] = []

        for s,d,w in edges:
            adj[s].append([d,w])
        
        shortest={} # map vertex -> distance of shortest path
        minHeap = [[0,src]]
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1+w2, n2])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest

sol = Solution()
print(sol.shortestPath(n=5, edges=[[0,1,10],[0,2,3],[1,3,2],[2,1,4],[2,3,8],[2,4,2],[3,4,5]], src=0))
