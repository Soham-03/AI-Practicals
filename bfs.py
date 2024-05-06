from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])  # Initialize the queue with the start node
    
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from queue
        if vertex not in visited:
            print(vertex, end=' ')  # Output the node, you can remove this line if not needed
            visited.add(vertex)
            # Enqueue all adjacent nodes that are not visited
            queue.extend(n for n in graph[vertex] if n not in visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
bfs(graph, start_node)
