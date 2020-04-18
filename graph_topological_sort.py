from collections import deque

def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order
    in_degree = {i:0 for i in range(vertices)}
    graph = {i:[] for i in range(vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1
    
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                