import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity and set start node to 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue: (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we have already found a better path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If found shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
# Define the graph as an adjacency list
graph = {
    'A': [('B', 4), ('H', 8)],
    'B': [('C', 8), ('H', 11)],
    'C': [('D', 7), ('I', 2),('F', 4)],
    'D': [('E', 9), ('F', 14)],
    'E': [('F',10), ('D', 9)],
    'F': [('C', 4), ('G', 2)],
    'G': [('I', 6), ('H', 1)],
    'H': [('G', 1), ('I', 7)],
    'I': [('G', 6), ('H', 7),('C', 2)],
}


start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
