from data_loader import DataLoader
from graph import Graph
from config import DATA_PATH

class RouteOptimizer:
    """
    Handles the process of building a graph from UPS facilities data
    and computing the optimal route between two locations.
    """

    def __init__(self):
        """
        Initializes the Route Optimizer by loading the UPS facility data
        and constructing the graph.
        """
        self.graph = Graph()
        self.data_loader = DataLoader(DATA_PATH)
        self._build_graph()

    def _build_graph(self):
        """
        Loads UPS facility data and populates the graph with nodes and edges.
        """
        facilities = self.data_loader.get_facilities()

        # Add nodes
        for _, row in facilities.iterrows():
            self.graph.add_node(row["NAME"], row["LATITUDE"], row["LONGITUDE"])

        # Example: Adding sample edges (in a real scenario, we should use API/real transit data)
        for i in range(len(facilities) - 1):
            node1 = facilities.iloc[i]["NAME"]
            node2 = facilities.iloc[i + 1]["NAME"]
            self.graph.add_edge(node1, node2, 10)  # Example weight (transit time)

    def find_best_route(self, start, end, algorithm="a_star"):
        """
        Finds the best route between two UPS facilities.

        Parameters:
        - start (str): Starting facility name.
        - end (str): Destination facility name.
        - algorithm (str): Algorithm choice ("dijkstra" or "a_star").

        Returns:
        - tuple: (shortest_path_list, total_cost)
        """
        if algorithm == "dijkstra":
            return self.graph.dijkstra(start, end)
        elif algorithm == "a_star":
            return self.graph.a_star(start, end)
        else:
            raise ValueError("Invalid algorithm choice. Use 'dijkstra' or 'a_star'.")

# Usage Example
if __name__ == "__main__":
    optimizer = RouteOptimizer()
    start_location = input("Enter the start facility: ").strip()
    end_location = input("Enter the destination facility: ").strip()
    algorithm_choice = input("Choose algorithm (dijkstra / a_star): ").strip().lower()

    if algorithm_choice not in ["dijkstra", "a_star"]:
        print("Invalid algorithm. Defaulting to A*.")
        algorithm_choice = "a_star"

    route, cost = optimizer.find_best_route(start_location, end_location, algorithm=algorithm_choice)
    print(f"Optimal Route: {route} with cost: {cost}")
