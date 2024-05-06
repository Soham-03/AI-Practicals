import random

# Define the function to maximize
def objective_function(x):
    return -(x - 3)**2 + 4

# Define the function for the Hill Climbing algorithm
def hill_climbing():
    # Start with a random solution in the range of -10 to 10
    current_solution = random.uniform(-10, 10)
    current_value = objective_function(current_solution)
    
    # Number of iterations and step size for generating neighbors
    steps = 1000
    step_size = 0.1
    
    for _ in range(steps):
        # Generate a neighbor by adding or subtracting the step size
        neighbor = current_solution + random.choice([-step_size, step_size])
        neighbor_value = objective_function(neighbor)
        
        # If the neighbor is better, move to the neighbor
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
            print(f"New better solution found: x = {current_solution}, f(x) = {current_value}")
    
    return current_solution, current_value

# Run the Hill Climbing algorithm
best_solution, best_value = hill_climbing()
print(f"Best solution: x = {best_solution}, f(x) = {best_value}")
