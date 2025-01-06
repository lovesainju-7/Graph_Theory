import networkx as nx
from geopy.distance import geodesic
import time

# Dijkstra Algorithm
def dijkstra_algorithm(G, source, target):
    return nx.dijkstra_path(G, source=source, target=target, weight='weight')

# Bellman-Ford Algorithm
def bellman_ford_algorithm(G, source, target):
    return nx.bellman_ford_path(G, source=source, target=target, weight='weight')

# A* Algorithm
def a_star_algorithm(G, source, target):
    def heuristic(node1, node2):
        pos1 = G.nodes[node1]['pos']
        pos2 = G.nodes[node2]['pos']
        return geodesic((pos1[1], pos1[0]), (pos2[1], pos2[0])).kilometers

    return nx.astar_path(G, source=source, target=target, weight='weight', heuristic=heuristic)

# Compare Routing Algorithms
def compare_routing_algorithms(G, source, target):
    # Compare Dijkstra
    print("\nDijkstra Algorithm:")
    start = time.time()
    dijkstra_path = dijkstra_algorithm(G, source, target)
    dijkstra_time = time.time() - start
    print(f"Shortest Path: {dijkstra_path}")
    print(f"Execution Time: {dijkstra_time:.6f} seconds")
    
    # Compare Bellman-Ford
    print("\nBellman-Ford Algorithm:")
    start = time.time()
    bellman_ford_path = bellman_ford_algorithm(G, source, target)
    bellman_ford_time = time.time() - start
    print(f"Shortest Path: {bellman_ford_path}")
    print(f"Execution Time: {bellman_ford_time:.6f} seconds")
    
    # Compare A* Algorithm
    print("\nA* Algorithm:")
    start = time.time()
    try:
        a_star_path = a_star_algorithm(G, source, target)
        a_star_time = time.time() - start
        print(f"Shortest Path: {a_star_path}")
        print(f"Execution Time: {a_star_time:.6f} seconds")
    except nx.NetworkXNoPath:
        print("No path exists.")
    except Exception as e:
        print(f"Error: {e}")
