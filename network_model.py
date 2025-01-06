import networkx as nx
from geopy.distance import geodesic

# Function to create the network graph
def create_network_graph(threshold=2000, latency_per_km=0.1):
    servers = {
        "Beijing (F-Root)": (39.908657170664284, 116.40744366071854),
        "Ulaanbaatar (I-Root)": (47.925489761874566, 106.90519368487101),
        "Seoul (F-Root)": (37.570588255250925, 126.97830876553707),
        "Tokyo (K-Root)": (35.69364076859484, 139.6927315206505),
        "Kathmandu (J-Root)": (27.697480843101093, 85.32595514492928),
        "Thimphu (K-Root)": (27.432195344458957, 89.65136832598677),
        "Delhi (K-Root)": (28.709454485241707, 77.10214292911624),
        "Dhaka (F-Root)": (23.716286807244927, 90.40727417333864),
        "Karachi (F-Root)": (24.89771625685946, 67.02805591279059),
        "Mumbai (I-Root)": (19.080856668920223, 72.8773231136106),
        "Chennai (F-Root)": (13.058335239832585, 80.25131212386664),
        "Colombo (I-Root)": (6.934210101363445, 79.86080739213143),
        "Bangkok (I-Root)": (13.733291322371999, 100.52383789110326),
        "Phnom Penh (F-Root)": (11.565871238891692, 104.9181323207523),
        "Kuala Lumpur (I-Root)": (3.13842431601014, 101.68487871056935),
        "Jakarta (I-Root)": (-6.169617943221922, 106.86500690789407),
        "Singapore (F-Root)": (1.359289361789639, 103.81914483670622),
        "Manila (I-Root)": (14.605478137135725, 120.98524509935208),
        "Taipei (K-Root)": (25.079091582404914, 121.57650285075167),
        "Hongkong (F-Root)": (22.402082576524865, 114.10929040891995),
    }
    
    G = nx.Graph()
    
    for server, location in servers.items():
        G.add_node(server, pos=(location[1], location[0]))  # Store longitude and latitude for plotting

    for server1, loc1 in servers.items():
        for server2, loc2 in servers.items():
            if server1 != server2:
                distance = geodesic(loc1, loc2).kilometers
                if distance <= threshold:
                    latency = distance * latency_per_km  # Simulate latency
                    G.add_edge(server1, server2, weight=latency)

    return G