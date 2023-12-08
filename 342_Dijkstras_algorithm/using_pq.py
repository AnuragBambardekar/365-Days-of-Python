import heapq

def dijkstra(graph, start):
    # Step 1: Initialize distance values and priority queue
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        # Step 3: Extract the node with the minimum distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Step 2: Update distances of neighbors and insert them into the priority queue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
result = dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}: {result}")
