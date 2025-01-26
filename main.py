from network_model import create_network_graph, create_sparse_network, create_dense_network
from algorithms import compare_routing_algorithms, analyze_efficiency_for_large_graph, visualize_network, test_scalability

# Main execution
if __name__ == "__main__":
    # Create the network graph
    G = create_network_graph()

    # Specify the source and target nodes to test routing algorithms
    source = "Beijing (F-Root)"
    target = "Colombo (I-Root)"

    # Compare the routing algorithms
    compare_routing_algorithms(G, source, target)

    # Analyze the efficiency of the algorithms for large graphs
    analyze_efficiency_for_large_graph(G, source, target)

    # Test scalability
    test_scalability()

    # Test on sparse and dense networks
    print("\nTesting on Sparse Network:")
    sparse_G = create_sparse_network()
    compare_routing_algorithms(sparse_G, source, target)

    print("\nTesting on Dense Network:")
    dense_G = create_dense_network()
    compare_routing_algorithms(dense_G, source, target)

    # Visualize the network and the shortest path
    visualize_network(G, source, target)