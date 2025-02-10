import heapq
import math

class Node:
    """
    Represents a UPS facility in the graph.
    """

    def __init__(self, name, latitude, longitude):
        """
        Initializes a Node.

        Parameters:
        - name (str): Facility name.
        - latitude (float): GPS latitude.
        - longitude (float): GPS longitude.
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.edges = []  # List of (neighbor, weight)

    def add_edge(self, neighbor, weight):
        """
        Adds an edge (connection) to another node.

        Parameters:
        - neighbor (Node): Destination node.
        - weight (float): Transit time or cost.
        """
        self.edges.append((neighbor, weight))

    def __repr__(self):
        return f"Node({self.name}, {self.latitude}, {self.longitude})"


class Graph:
    """
    Represents a graph where nodes are UPS locations and edges are transit routes.
    """

    def __init__(self):
        self.nodes = {}  # Dictionary of all nodes

    def add_node(self, name, latitude, longitude):
        """
        Adds a new node to the graph.

        Parameters:
        - name (str): Facility name.
        - latitude (float): GPS latitude.
        - longitude (float): GPS longitude.
        """
        if name not in self.nodes:
            self.nodes[name] = Node(name, latitude, longitude)

    def add_edge(self, node1_name, node2_name, weight):
        """
        Adds a bidirectional edge between two nodes.

        Parameters:
        - node1_name (str): Name of the first facility.
        - node2_name (str): Name of the second facility.
        - weight (float): Transit time or cost.
        """
        if node1_name in self.nodes and node2_name in self.nodes:
            self.nodes[node1_name].add_edge(self.nodes[node2_name], weight)
            self.nodes[node2_name].add_edge(self.nodes[node1_name], weight)  # Bidirectional
        else:
            raise ValueError("One or both nodes not found in the graph.")

    def dijkstra(self, start_name, end_name):
        """
        Finds the shortest path between two nodes using Dijkstra’s algorithm.

        Parameters:
        - start_name (str): Starting facility.
        - end_name (str): Destination facility.

        Returns:
        - tuple: (shortest_path_list, total_cost)
        """
        if start_name not in self.nodes or end_name not in self.nodes:
            raise ValueError("Start or end node not found in the graph.")

        heap = [(0, start_name)]  
        distances = {node: float('inf') for node in self.nodes}
        distances[start_name] = 0
        predecessors = {}

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_node == end_name:
                break

            for neighbor, weight in self.nodes[current_node].edges:
                distance = current_distance + weight
                if distance < distances[neighbor.name]:
                    distances[neighbor.name] = distance
                    predecessors[neighbor.name] = current_node
                    heapq.heappush(heap, (distance, neighbor.name))

        # Construct shortest path
        path, node = [], end_name
        while node in predecessors:
            path.insert(0, node)
            node = predecessors[node]

        if path:
            path.insert(0, start_name)

        return path, distances[end_name]

    def heuristic(self, node1, node2):
        """
        Heuristic function for A* (Haversine distance between two locations).

        Parameters:
        - node1 (Node): Starting node.
        - node2 (Node): Goal node.

        Returns:
        - float: Estimated distance between nodes.
        """
        lat1, lon1 = math.radians(node1.latitude), math.radians(node1.longitude)
        lat2, lon2 = math.radians(node2.latitude), math.radians(node2.longitude)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        R = 6371  # Radius of Earth in km
        return R * c  # Distance in km

    def a_star(self, start_name, end_name):
        """
        Finds the shortest path using the A* algorithm.

        Parameters:
        - start_name (str): Starting facility.
        - end_name (str): Destination facility.

        Returns:
        - tuple: (shortest_path_list, total_cost)
        """
        if start_name not in self.nodes or end_name not in self.nodes:
            raise ValueError("Start or end node not found in the graph.")

        start_node = self.nodes[start_name]
        end_node = self.nodes[end_name]

        heap = [(0, start_name)]  # Priority queue
        distances = {node: float('inf') for node in self.nodes}
        distances[start_name] = 0
        predecessors = {}

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            if current_node == end_name:
                break

            for neighbor, weight in self.nodes[current_node].edges:
                distance = current_distance + weight
                heuristic_cost = distance + self.heuristic(neighbor, end_node)

                if distance < distances[neighbor.name]:
                    distances[neighbor.name] = distance
                    predecessors[neighbor.name] = current_node
                    heapq.heappush(heap, (heuristic_cost, neighbor.name))

        # Construct shortest path
        path, node = [], end_name
        while node in predecessors:
            path.insert(0, node)
            node = predecessors[node]

        if path:
            path.insert(0, start_name)

        return path, distances[end_name]

    def __repr__(self):
        return f"Graph({len(self.nodes)} nodes)"
