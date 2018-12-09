"""
The below algorithm takes in a graph G
and start vertex. It returns all possible
nodes that one can visit starting at the
vertex given

"""

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def dfs(graph, vertex):
    visited = set()
    stack = [vertex]
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node]
            for neighbor in neighbors:
                stack.append(neighbor)
    return visited
