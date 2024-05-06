def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end = '')

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
dfs(graph, start_node)
