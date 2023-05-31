class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def bellman_ford(edges, start_node, num_nodes):
    distances = [float('inf')] * num_nodes
    distances[start_node] = 0
    
    for _ in range(num_nodes - 1):
        for edge in edges:
            if distances[edge.source] + edge.weight < distances[edge.destination]:
                distances[edge.destination] = distances[edge.source] + edge.weight
    
    # Periksa adanya siklus negatif
    for edge in edges:
        if distances[edge.source] + edge.weight < distances[edge.destination]:
            raise ValueError("Graf mengandung siklus negatif")
    
    return distances

# Contoh penggunaan algoritma Bellman-Ford untuk memecahkan permasalahan cerita
edges = [
    Edge(0, 1, 4),  # Kota 0 ke Kota 1 dengan jarak 4
    Edge(0, 2, 2),  # Kota 0 ke Kota 2 dengan jarak 2
    Edge(1, 3, 3),  # Kota 1 ke Kota 3 dengan jarak 3
    Edge(2, 1, -2), # Kota 2 ke Kota 1 dengan jarak -2 (jalur rusak)
    Edge(2, 3, 5),  # Kota 2 ke Kota 3 dengan jarak 5
    Edge(3, 4, 1),  # Kota 3 ke Kota 4 dengan jarak 1
]

start_node = 0
num_nodes = 5

try:
    shortest_distances = bellman_ford(edges, start_node, num_nodes)
    for i, distance in enumerate(shortest_distances):
        print(f"Jarak terpendek dari Kota {start_node} ke Kota {i}: {distance}")
except ValueError as e:
    print(str(e))
