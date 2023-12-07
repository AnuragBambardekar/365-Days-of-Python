"""
Graph coloring is a fundamental problem in computer science and mathematics. The goal is to assign colors to the vertices of a graph 
in such a way that no two adjacent vertices share the same color. This problem has various applications, including register 
allocation in compilers, scheduling, and map coloring.

One of the well-known algorithms for graph coloring is the Greedy Coloring algorithm. Here's a basic outline of the algorithm:

Start with an empty color assignment.
For each vertex in the graph:
a. Assign the lowest available color to the vertex that is not used by its neighbors.
b. If all colors are used by neighbors, assign a new color to the vertex.
The resulting color assignment is a valid graph coloring.
"""

def greedy_coloring(graph):
    colors = {}  # Dictionary to store color assignments for each vertex

    for vertex in graph:
        used_colors = set(colors[neighbor] for neighbor in graph[vertex] if neighbor in colors)

        for color in range(len(graph)):
            if color not in used_colors:
                colors[vertex] = color
                break

    return colors

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

result = greedy_coloring(graph)
print(result)
