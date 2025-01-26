import time
import networkx as nx
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import random

# Dijkstra Algorithm to find the shortest path
def dijkstra_algorithm(G, source, target):
    try:
        path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
        return path
    except nx.NetworkXNoPath:
        print(f"No path exists between {source} and {target} using Dijkstra.")
        return None

# Bellman-Ford Algorithm to handle graphs with negative edge weights
def bellman_ford_algorithm(G, source, target):
    try:
        path = nx.bellman_ford_path(G, source=source, target=target, weight='weight')
        return path
    except nx.NetworkXUnbounded:
        print("Negative weight cycle detected. Bellman-Ford cannot compute shortest paths.")
        return None
    except nx.NetworkXNoPath:
        print(f"No path exists between {source} and {target} using Bellman-Ford.")
        return None

# A* Algorithm with heuristic based on geodesic distance
def a_star_algorithm(G, source, target):
    def heuristic(node1, node2):
        pos1 = G.nodes[node1]['pos']
        pos2 = G.nodes[node2]['pos']
        # Ensure the heuristic is admissible (never overestimates the cost)
        return geodesic((pos1[1], pos1[0]), (pos2[1], pos2[0])).kilometers  # lat, lon

    try:
        path = nx.astar_path(G, source=source, target=target, weight='weight', heuristic=heuristic)
        return path
    except nx.NetworkXNoPath:
        print(f"No path exists between {source} and {target} using A*.")
        return None
    except Exception as e:
        print(f"Error in A* Algorithm: {e}")
        return None

# Function to calculate energy consumption
def calculate_energy_consumption(path, G):
    energy = 0
    for i in range(len(path) - 1):
        # Energy consumption is proportional to latency and distance
        latency = G.edges[path[i], path[i + 1]]['weight']
        energy += latency * 0.01  # Simulated energy consumption factor
    return energy

# Function to simulate packet delivery
def simulate_packet_delivery(path, G):
    packet_loss_probability = 0.1  # 10% chance of packet loss per hop
    successful_delivery = 1.0
    for i in range(len(path) - 1):
        latency = G.edges[path[i], path[i + 1]]['weight']
        if random.random() < packet_loss_probability:
            successful_delivery *= (1 - packet_loss_probability)
    return successful_delivery

# Function to compare all routing algorithms and print results
def compare_routing_algorithms(G, source, target):
    # Compare Dijkstra
    print("\nDijkstra Algorithm:")
    dijkstra_path = dijkstra_algorithm(G, source, target)
    if dijkstra_path:
        print(f"Shortest Path from {source} to {target}: {dijkstra_path}")
        print(f"Total Latency: {sum(G.edges[u, v]['weight'] for u, v in zip(dijkstra_path[:-1], dijkstra_path[1:]))}")
        print(f"Energy Consumption: {calculate_energy_consumption(dijkstra_path, G)}")
        print(f"Packet Delivery Success Rate: {simulate_packet_delivery(dijkstra_path, G)}")

    # Compare Bellman-Ford
    print("\nBellman-Ford Algorithm:")
    bellman_ford_path = bellman_ford_algorithm(G, source, target)
    if bellman_ford_path:
        print(f"Shortest Path from {source} to {target}: {bellman_ford_path}")
        print(f"Total Latency: {sum(G.edges[u, v]['weight'] for u, v in zip(bellman_ford_path[:-1], bellman_ford_path[1:]))}")
        print(f"Energy Consumption: {calculate_energy_consumption(bellman_ford_path, G)}")
        print(f"Packet Delivery Success Rate: {simulate_packet_delivery(bellman_ford_path, G)}")

    # Compare A* Algorithm
    print("\nA* Algorithm:")
    a_star_path = a_star_algorithm(G, source, target)
    if a_star_path:
        print(f"A* Path from {source} to {target}: {a_star_path}")
        print(f"Total Latency: {sum(G.edges[u, v]['weight'] for u, v in zip(a_star_path[:-1], a_star_path[1:]))}")
        print(f"Energy Consumption: {calculate_energy_consumption(a_star_path, G)}")
        print(f"Packet Delivery Success Rate: {simulate_packet_delivery(a_star_path, G)}")

# Efficiency analysis for large graphs
def analyze_efficiency_for_large_graph(G, source, target):
    # Measure execution time of Dijkstra
    start_time = time.time()
    dijkstra_path = dijkstra_algorithm(G, source, target)
    dijkstra_time = time.time() - start_time
    print(f"\nDijkstra Algorithm execution time: {dijkstra_time:.6f} seconds")
    
    # Measure execution time of Bellman-Ford
    start_time = time.time()
    bellman_ford_path = bellman_ford_algorithm(G, source, target)
    bellman_ford_time = time.time() - start_time
    print(f"Bellman-Ford Algorithm execution time: {bellman_ford_time:.6f} seconds")
    
    # Measure execution time of A*
    start_time = time.time()
    a_star_path = a_star_algorithm(G, source, target)
    a_star_time = time.time() - start_time
    print(f"A* Algorithm execution time: {a_star_time:.6f} seconds")
    
    # Check correctness: Compare paths with the built-in shortest path
    print("\nPath Correctness Analysis:")
    try:
        nx_shortest_path = nx.shortest_path(G, source=source, target=target, weight='weight')
        print(f"NetworkX shortest path: {nx_shortest_path}")
        print(f"Dijkstra path matches NetworkX: {dijkstra_path == nx_shortest_path}")
        print(f"Bellman-Ford path matches NetworkX: {bellman_ford_path == nx_shortest_path}")
        print(f"A* path matches NetworkX: {a_star_path == nx_shortest_path}")
    except Exception as e:
        print(f"Error in shortest path computation: {e}")

# Function to visualize the network and the shortest path
def visualize_network(G, source, target):
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=8)
    
    # Highlight the shortest path using Dijkstra
    dijkstra_path = dijkstra_algorithm(G, source, target)
    if dijkstra_path:
        path_edges = list(zip(dijkstra_path[:-1], dijkstra_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.title(f"Shortest Path from {source} to {target}")
    plt.show()

# Function to test scalability of algorithms
def test_scalability():
    sizes = [10, 50, 100, 200]  # Number of nodes
    for size in sizes:
        G = nx.random_geometric_graph(size, radius=0.2)
        for u, v in G.edges():
            G.edges[u, v]['weight'] = random.uniform(1, 10)  # Random edge weights
        
        source = random.choice(list(G.nodes()))
        target = random.choice(list(G.nodes()))
        
        print(f"\nTesting scalability for {size} nodes:")
        analyze_efficiency_for_large_graph(G, source, target)