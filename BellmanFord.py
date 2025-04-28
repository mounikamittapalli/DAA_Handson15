def bellman_ford(graph, vertices, start):
    distance = {v: float('inf') for v in vertices}
    distance[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distance

# Edge list
graph = [
    ('S', 'T', 6),
    ('S', 'Y', 7),
    ('Y', 'Z', 9),
    ('Y', 'X', -3),
    ('T', 'X', 5),
    ('T', 'Y', 8),
    ('T', 'Z', -4),
    ('Z', 'X', 7),
    ('Z', 'S', 2),
    ('X', 'T', -2)
]

# Only include valid vertices
vertices = ['S', 'T', 'Y', 'Z', 'X']
start_node = 'S'

shortest_paths = bellman_ford(graph, vertices, start_node)
print(shortest_paths)
