from route_optimizer import RouteOptimizer

def main():
    """
    Main function to run the Supply Chain Route Optimization program.
    """
    print("Initializing Route Optimizer...")
    optimizer = RouteOptimizer()

    # Get user input for start and end locations
    start_location = input("Enter the start facility name: ").strip()
    end_location = input("Enter the destination facility name: ").strip()

    # Choose Algorithm: "dijkstra" or "a_star"
    algorithm_choice = input("Choose algorithm (dijkstra / a_star): ").strip().lower()
    
    if algorithm_choice not in ["dijkstra", "a_star"]:
        print("Invalid algorithm choice. Defaulting to A*.")
        algorithm_choice = "a_star"

    print(f"Finding best route from {start_location} to {end_location} using {algorithm_choice} algorithm...")

    try:
        route, cost = optimizer.find_best_route(start_location, end_location, algorithm=algorithm_choice)
        print(f"Optimal Route: {route}")
        print(f"Total Cost (Transit Time): {cost}")
    except Exception as e:
        print(f"Error finding route: {e}")

if __name__ == "__main__":
    main()
