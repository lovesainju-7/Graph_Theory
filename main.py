from network_model import create_network_graph
from algorithms import compare_routing_algorithms

# Create the network graph
G = create_network_graph(threshold=2000, latency_per_km=0.1)

# Define source and target nodes
source = "Beijing (F-Root)"
target = "Colombo (I-Root)"

# Compare the routing algorithms
compare_routing_algorithms(G, source, target)