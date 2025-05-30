from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph , start):
    visited = set()
    queue = deque([start])


    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)



def dfs (node , visited = none):
    if visited is none:
        visited = set()

    if node not in visited:
        visited.add(node)
        for neighbour in graph[node ]:
            dfs(neighbour, visited)    



