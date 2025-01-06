import networkx as nx
from geopy.distance import geodesic
import random

# Server data with location details
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
    "Sydney (I-Root)": (-33.8688197, 151.2092955),  # Adding an example Australian server
    "Auckland (I-Root)": (-36.848459, 174.763332),  # Adding an example New Zealand server
    "Cape Town (I-Root)": (-33.9248685, 18.4232202),  # Adding an example South African server
    "London (F-Root)": (51.507351, -0.127758),  # Adding an example UK server
    "New York (I-Root)": (40.712776, -74.005974),  # Adding an example US server
    "Rio de Janeiro (I-Root)": (-22.906847, -43.172896),  # Adding an example Brazil server
    "Paris (F-Root)": (48.856613, 2.352222),  # Adding an example France server
    "Moscow (I-Root)": (55.755825, 37.617298),  # Adding an example Russia server
    "Berlin (F-Root)": (52.520008, 13.404954),  # Adding an example Germany server
    "Buenos Aires (I-Root)": (-34.603684, -58.381559),  # Adding an example Argentina server
}

# Function to simulate dynamic factors affecting latency
def get_dynamic_latency(distance):
    # Simulate weather effects (e.g., 1.2x latency during bad weather)
    weather_factor = random.uniform(1.0, 1.3)  # Random factor between 1.0 and 1.3

    # Simulate server downtime (e.g., 10% chance of server downtime)
    downtime_factor = random.choice([1, float('inf')])  # 1 means no downtime, inf means downtime
    
    if downtime_factor == float('inf'):
        return float('inf')  # Server is down, set latency to infinity

    return distance * 0.1 * weather_factor  # Simulated latency with a weather factor

# Function to create the network graph with dynamic latency
def create_network_graph(threshold=2000):
    G = nx.Graph()

    # Adding nodes
    for server, location in servers.items():
        G.add_node(server, pos=(location[1], location[0]))  # Longitude, Latitude

    # Adding edges with dynamic latency
    for server1, loc1 in servers.items():
        for server2, loc2 in servers.items():
            if server1 != server2:
                distance = geodesic(loc1, loc2).kilometers
                if distance <= threshold:
                    latency = get_dynamic_latency(distance)  # Apply dynamic latency
                    G.add_edge(server1, server2, weight=latency)

    return G
