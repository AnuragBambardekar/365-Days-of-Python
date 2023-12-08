# Dijkstra's Algorithm

- Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a weighted graph, which may represent, for example, road networks. 
- It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published 3 years later.

The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

## Algorithm

The algorithm maintains a set of visited vertices and a set of unvisited vertices. It starts at the source vertex and iteratively selects the unvisited vertex with the smallest tentative distance from the source. It then visits the neighbors of this vertex and updates their tentative distances if a shorter path is found. This process continues until the destination vertex is reached, or all reachable vertices have been visited.

1. Mark the source node with a current distance of 0 and the rest with infinity.
2. Set the non-visited node with the smallest current distance as the current node.
3. For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1. If it is smaller than the current distance of Node, set it as the new current distance of N.
4. Mark the current node 1 as visited.
5. Go to step 2 if there are any nodes are unvisited.

There are several ways to Implement Dijkstra’s algorithm, but the most common ones are:

- Priority Queue (Heap-based Implementation)
    1. Initialize the distance values and priority queue.
    2. Insert the source node into the priority queue with distance 0.
    3. While the priority queue is not empty:
        - Extract the node with the minimum distance from the priority queue.
        - Update the distances of its neighbors if a shorter path is found.
        - Insert updated neighbors into the priority queue.

- Array-based Implementation 
    1. Initialize an array to store distances from the source to each node.
    2. Mark all nodes as unvisited.
    3. Set the distance to the source node as 0 and infinity for all other nodes.
    4. Repeat until all nodes are visited:
        - Find the unvisited node with the smallest known distance.
        - For the current node, update the distances of its unvisited neighbors.
        - Mark the current node as visited.

    *can be less efficient, especially on large graphs*

## Applicability

- Dijkstra’s algorithm can work on both directed graphs and undirected graphs as this algorithm is designed to work on any type of graph as long as it meets the requirements of having non-negative edge weights and being connected.

    - In a directed graph, each edge has a direction, indicating the direction of travel between the vertices connected by the edge. In this case, the algorithm follows the direction of the edges when searching for the shortest path.
    - In an undirected graph, the edges have no direction, and the algorithm can traverse both forward and backward along the edges when searching for the shortest path.

## Similar Algortihms to find shortest path

| Feature | Dijkstra's | Bellman Ford | Floyd-Warshall |
|---------| ---------- | ------------ | ------------ |
|Optimization| Optimized for finding the shortest path between a single source node and all other nodes in a graph with non-negative edge weights | Bellman-Ford algorithm is optimized for finding the shortest path between a single source node and all other nodes in a graph with negative edge weights. | Floyd-Warshall algorithm is optimized for finding the shortest path between all pairs of nodes in a graph. | A* algorithm is an informed search algorithm that uses a heuristic function to guide the search towards the goal node. |
|Relaxation/Heuristic Function| Dijkstra’s algorithm uses a greedy approach where it chooses the node with the smallest distance and updates its neighbors	| the Bellman-Ford algorithm relaxes all edges in each iteration, updating the distance of each node by considering all possible paths to that node| Floyd-Warshall algorithm, on the other hand, is an all-pairs shortest path algorithm that uses dynamic programming to calculate the shortest path between all pairs of nodes in the graph. | A* algorithm uses a heuristic function that estimates the distance from the current node to the goal node. This heuristic function is admissible, meaning that it never overestimates the actual distance to the goal node |
|Time Complexity|	Dijkstra’s algorithm has a time complexity of O(V^2) for a dense graph and O(E log V) for a sparse graph, where V is the number of vertices and E is the number of edges in the graph.|	Bellman-Ford algorithm has a time complexity of O(VE), where V is the number of vertices and E is the number of edges in the graph.| Floyd-Warshall algorithm, on the other hand, is an all-pairs shortest path algorithm that uses dynamic programming to calculate the shortest path between all pairs of nodes in the graph. | The time complexity of A* algorithm depends on the quality of the heuristic function. |
|Negative Weights|	Dijkstra’s algorithm does not work with graphs that have negative edge weights, as it assumes that all edge weights are non-negative.|	Bellman-Ford algorithm can handle negative edge weights and can detect negative-weight cycles in the graph.| Floyd-Warshall algorithm, on the other hand, is an all-pairs shortest path algorithm that uses dynamic programming to calculate the shortest path between all pairs of nodes in the graph. |  A* algorithm is commonly used in pathfinding and graph traversal problems, such as video games, robotics, and planning algorithms. |