from helper import *
import copy

with open("day6.txt", "r") as f:
    original_map = [list(line.strip()) for line in f]

# Directions in order: up, right, down, left
directions = ["up", "right", "down", "left"]
direction_vectors = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

# Find all empty positions where we can place an obstruction
empty_positions = []
for row in range(len(original_map)):
    for col in range(len(original_map[row])):
        if original_map[row][col] == ".":
            empty_positions.append((row, col))

successful_simulations = 0

for obstruction in empty_positions:
    # Create a copy of the map for each simulation
    map_copy = copy.deepcopy(original_map)
    map_copy[obstruction[0]][obstruction[1]] = "#"

    # Locate the guard's starting position and initial direction
    guard_position = None
    for row in range(len(map_copy)):
        for col in range(len(map_copy[row])):
            if map_copy[row][col] in ["^", ">", "v", "<"]:
                guard_position = (row, col)
                if map_copy[row][col] == "^":
                    direction = "up"
                elif map_copy[row][col] == ">":
                    direction = "right"
                elif map_copy[row][col] == "v":
                    direction = "down"
                elif map_copy[row][col] == "<":
                    direction = "left"
                break
        if guard_position is not None:
            break

    if guard_position is None:
        continue  # No guard found, skip this simulation

    visited_states = set()
    loop_detected = False

    while True:
        state = (guard_position, direction)
        if state in visited_states:
            # Loop detected
            loop_detected = True
            break
        visited_states.add(state)

        # Calculate next position
        delta = direction_vectors[direction]
        next_position = (guard_position[0] + delta[0], guard_position[1] + delta[1])

        # Check if next position is within bounds
        if not is_within_bounds(next_position, map_copy):
            # Guard exits the map
            break

        # Check if there's an obstruction ahead
        if map_copy[next_position[0]][next_position[1]] == "#":
            # Turn right
            dir_index = directions.index(direction)
            direction = directions[(dir_index + 1) % 4]
        else:
            # Move forward
            guard_position = next_position

    if loop_detected:
        successful_simulations += 1

print(f"Number of successful simulations: {successful_simulations}")