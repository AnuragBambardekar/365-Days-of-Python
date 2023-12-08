def dijkstra_array(graph, start):
    # Step 1: Initialize array to store distances
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Step 2: Mark all nodes as unvisited
    unvisited_nodes = set(graph.keys())

    while unvisited_nodes:
        # Step 4: Find the unvisited node with the smallest known distance
        current_node = min(unvisited_nodes, key=lambda node: distances[node])

        # Step 3: Set the distance to the source node as 0 and infinity for other nodes
        if distances[current_node] == float('infinity'):
            break

        # Step 4 (cont.): For the current node, update the distances of its unvisited neighbors
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Mark the current node as visited
        unvisited_nodes.remove(current_node)

    return distances

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
result = dijkstra_array(graph, start_node)
print(f"Shortest distances from node {start_node}: {result}")
