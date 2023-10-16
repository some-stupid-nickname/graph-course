
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0


    visited = set()

    while True:
        min_distance = float('inf')
        min_node = None
        for node in graph:
            if distances[node] < min_distance and node not in visited:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            break
        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances



#А вот тут проверку делаем

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

start_node = 'C'
distances = dijkstra(graph, start_node)

print("Расстояния до вершин от стартовой вершины", start_node, ":")
for node, distance in distances.items():
    print("Вершина:", node, ", Расстояние:", distance)