from collections import deque

graph = {
    'A': ['B', 'C'],
    'B' : ["D","E"],
    'C' : ["F"],
    'D' : [],
    'E' : [],
    'F' : []
}

def bfs(graph , start):
    visited = set()
    queue = deque([start])
    result = []