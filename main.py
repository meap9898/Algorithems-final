import heapq

# creates the method for the algorithm
def dijkstra(graph, start, stop):
    # Initialize distances with infinity for all nodes
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # start at zero
    # make a priority queue
    priority_queue = [(0, start)]
    visited = set()  # Keep track of visited nodes
    # Keep track of previous nodes to reconstruct the path
    previous = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # checks if the node has been visited
        if current_node in visited:
            continue

        # labels the node as visited
        visited.add(current_node)

        # ends the loop
        if current_node == stop:
            break

        # Explore neighbors of current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # changes the shortest if the new path found is shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the path
    path = []
    current = stop
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    # Adds up the cost to the shortest path
    total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))

    return distances, path, total_cost

# The data set
graph = {
    'A': {'B': 6, 'F': 5},
    'B': {'A': 6, 'C': 5, 'G': 6},
    'C': {'B': 5, 'D': 7, 'H': 5},
    'D': {'C': 7, 'E': 7, 'I': 8},
    'E': {'D': 7, 'I': 6, 'N': 15},
    'F': {'A': 5, 'G': 8, 'J': 7},
    'G': {'B': 6, 'F': 8, 'H': 9, 'K': 8},
    'H': {'G': 9, 'I': 12, 'C': 5},
    'I': {'D': 8, 'E': 6, 'H': 12, 'M': 10},
    'J': {'F': 7, 'K': 5, 'O': 7},
    'K': {'G': 8, 'J': 5, 'L': 7},
    'L': {'K': 7, 'M': 7, 'P': 7},
    'M': {'I': 10, 'L': 7, 'N': 9},
    'N': {'E': 15, 'M': 9, 'R': 7},
    'O': {'J': 7, 'P': 13, 'S': 9},
    'P': {'P': 13, 'L': 7, 'Q': 8, 'U': 11},
    'Q': {'P': 8, 'R': 9},
    'R': {'N': 7, 'Q': 9, 'W': 10},
    'S': {'O': 9, 'T': 9},
    'T': {'S': 9, 'U': 8},
    'U': {'T': 8, 'P': 11, 'V': 8},
    'V': {'U': 8, 'W': 5},
    'W': {'R': 10, 'V': 5}
}

starting = input("enter the start: ")
distanceH, pathH, costH = dijkstra(graph, starting, 'H')
distanceK, pathK, costK = dijkstra(graph, starting, 'K')
distanceQ, pathQ, costQ = dijkstra(graph, starting, 'Q')
distanceT, pathT, costT = dijkstra(graph, starting, 'T')
if (costH < costK and costH < costQ and costH < costT):
    print(f"Path: {pathH}, Cost: {costH}")
elif (costK < costH and costK < costQ and costK < costT):
    print(f"Path: {pathK}, Cost: {costK}")
elif (costQ < costH and costQ < costK and costQ < costT):
    print(f"Path: {pathQ}, Cost: {costQ}")
elif (costT < costH and costT < costK and costT < costQ):
    print(f"Path: {pathT}, Cost: {costT}")
