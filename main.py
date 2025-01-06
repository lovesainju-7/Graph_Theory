from network_model import create_network_graph
from algorithms import compare_routing_algorithms, analyze_efficiency_for_large_graph

# Create the network graph
G = create_network_graph()

# Specify the source and target nodes to test routing algorithms
source = "Beijing (F-Root)"
target = "Colombo (I-Root)"

# Compare the routing algorithms
compare_routing_algorithms(G, source, target)

# Analyze the efficiency of the algorithms for large graphs
analyze_efficiency_for_large_graph(G, source, target)