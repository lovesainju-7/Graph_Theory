import time
import networkx as nx
from geopy.distance import geodesic

# Dijkstra Algorithm to find the shortest path
def dijkstra_algorithm(G, source, target):
    return nx.dijkstra_path(G, source=source, target=target, weight='weight')

# Bellman-Ford Algorithm to handle graphs with negative edge weights
def bellman_ford_algorithm(G, source):
    return nx.bellman_ford_path(G, source=source, target=None, weight='weight')

# A* Algorithm (Heuristic is now defined correctly)
def a_star_algorithm(G, source, target):
    def heuristic(node1, node2):
        pos1 = G.nodes[node1]['pos']
        pos2 = G.nodes[node2]['pos']
        # Swap the coordinates to make sure it's in (latitude, longitude) order
        return geodesic((pos1[1], pos1[0]), (pos2[1], pos2[0])).kilometers  # lat, lon

    return nx.astar_path(G, source=source, target=target, weight='weight', heuristic=heuristic)

# Function to compare all routing algorithms and print results
def compare_routing_algorithms(G, source, target):
    # Compare Dijkstra
    print("\nDijkstra Algorithm:")
    dijkstra_path = dijkstra_algorithm(G, source, target)
    print(f"Shortest Path from {source} to {target}: {dijkstra_path}")

    # Compare Bellman-Ford
    print("\nBellman-Ford Algorithm:")
    bellman_ford_paths = bellman_ford_algorithm(G, source)
    print(f"Paths from {source}: {bellman_ford_paths}")

    # Compare A* Algorithm
    print("\nA* Algorithm:")
    try:
        a_star_path = a_star_algorithm(G, source, target)
        print(f"A* Path from {source} to {target}: {a_star_path}")
    except Exception as e:
        print(f"Error in A* Algorithm: {e}")

# Efficiency analysis for large graphs
def analyze_efficiency_for_large_graph(G, source, target):
    # Measure execution time of Dijkstra
    start_time = time.time()
    dijkstra_path = dijkstra_algorithm(G, source, target)
    dijkstra_time = time.time() - start_time
    print(f"Dijkstra Algorithm execution time: {dijkstra_time:.6f} seconds")
    
    # Measure execution time of Bellman-Ford
    start_time = time.time()
    bellman_ford_paths = bellman_ford_algorithm(G, source)
    bellman_ford_time = time.time() - start_time
    print(f"Bellman-Ford Algorithm execution time: {bellman_ford_time:.6f} seconds")
    
    # Measure execution time of A*
    start_time = time.time()
    try:
        a_star_path = a_star_algorithm(G, source, target)
        a_star_time = time.time() - start_time
        print(f"A* Algorithm execution time: {a_star_time:.6f} seconds")
    except Exception as e:
        print(f"Error in A* Algorithm: {e}")
    
    # Check correctness: Compare paths with the built-in shortest path
    print("\nPath Correctness Analysis:")
    try:
        nx_shortest_path = nx.shortest_path(G, source=source, target=target, weight='weight')
        print(f"NetworkX shortest path: {nx_shortest_path}")
        print(f"Dijkstra path matches NetworkX: {dijkstra_path == nx_shortest_path}")
    except Exception as e:
        print(f"Error in shortest path computation: {e}")
