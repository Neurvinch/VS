 graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


 def dfs(graph , start , visited = None , result = None ):
    if visited is None:
      visited = set()
    if result is None:
        result = []


    if start not in visited:
       result.append(start)
       visited.add(start)


    for neighbor in graph[start]:
       dfs(graph, neighbor, visited, result)

    return result