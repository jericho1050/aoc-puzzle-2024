
def move_guard(position, direction):
    # define the changes in position for each direciton

    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    # Get the current row and column
    row, col = position

    # Update the position based on the direction
    delta_row, delta_col = moves[direction]
    return (row + delta_row, col + delta_col)  # which is the new position

def is_within_bounds(position, map):
    row, col = position
    return 0 <= row < len(map) and 0 <= col < len(map[0])