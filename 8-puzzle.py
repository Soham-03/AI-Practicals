from heapq import heappop, heappush
from itertools import count

def manhattan_distance(state):
    """Calculate the Manhattan distance of the tiles from their goal positions."""
    distance = 0
    for idx, value in enumerate(state):
        if value != 0:
            target_x, target_y = divmod(value - 1, 3)
            current_x, current_y = divmod(idx, 3)
            distance += abs(target_x - current_x) + abs(target_y - current_y)
    return distance

def move_tile(state, empty_index, target_index):
    """Move the tile into the empty space."""
    new_state = list(state)
    new_state[empty_index], new_state[target_index] = new_state[target_index], new_state[empty_index]
    return tuple(new_state)

def get_neighbors(state):
    """Generate the states reachable from the current state."""
    empty_index = state.index(0)
    x, y = divmod(empty_index, 3)
    neighbors = []
    if x > 0:  # Move the empty space up
        neighbors.append(move_tile(state, empty_index, empty_index - 3))
    if x < 2:  # Move the empty space down
        neighbors.append(move_tile(state, empty_index, empty_index + 3))
    if y > 0:  # Move the empty space left
        neighbors.append(move_tile(state, empty_index, empty_index - 1))
    if y < 2:  # Move the empty space right
        neighbors.append(move_tile(state, empty_index, empty_index + 1))
    return neighbors

def solve_puzzle(initial_state):
    """Solve the 8-puzzle problem using the A* search algorithm."""
    target_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    if initial_state == target_state:
        return []

    priority_queue = []
    heappush(priority_queue, (manhattan_distance(initial_state), 0, initial_state, []))
    seen_states = set([initial_state])
    unique = count()

    while priority_queue:
        _, cost, state, path = heappop(priority_queue)

        for neighbor in get_neighbors(state):
            if neighbor in seen_states:
                continue

            if neighbor == target_state:
                return path + [neighbor]

            seen_states.add(neighbor)
            heappush(priority_queue, (cost + 1 + manhattan_distance(neighbor), next(unique), neighbor, path + [neighbor]))

    return None  # No solution found

# Example usage:
initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)
solution = solve_puzzle(initial_state)
print("Solution sequence:")
for step in solution:
    print(step)
