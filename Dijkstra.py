import heapq

def dijkstra(graph, start, goal):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    heap = [(0, start)]
    
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        
        if current_vertex == goal:
            break
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances[goal]

graph = {
    'A': {'B': 3, 'C': 5, 'D': 9},
    'B': {'A': 3, 'C': 2, 'E': 1},
    'C': {'A': 5, 'B': 2, 'D': 6, 'E': 4, 'F': 2},
    'D': {'A': 9, 'C': 6, 'F': 7},
    'E': {'B': 1, 'C': 4, 'F': 8, 'G': 2},
    'F': {'C': 2, 'D': 7, 'E': 8, 'G': 6},
    'G': {'E': 2, 'F': 6}
}

start = 'A'
goal = 'E'

shortest_distance = dijkstra(graph, start, goal)

print(f"Jarak terpendek dari gedung {start} ke gedung {goal} adalah: {shortest_distance}")
