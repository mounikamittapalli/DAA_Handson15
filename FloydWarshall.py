def floyd_warshall(graph):
    # Number of vertices
    V = len(graph)

    # Create a copy of the graph matrix to store distances
    dist = [row[:] for row in graph]

    # Main algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


    return dist
INF = float('inf')

# Adjacency matrix: graph[i][j] = weight from i to j
graph = [
    [0,   5, INF,30],
    [INF,   0, 5,20],
    [INF, INF,  0,5],
    [INF, INF, INF,0]
]

shortest_paths = floyd_warshall(graph)
for row in shortest_paths:
    print(row)
