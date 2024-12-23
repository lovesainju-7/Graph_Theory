# algorithms.py

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
