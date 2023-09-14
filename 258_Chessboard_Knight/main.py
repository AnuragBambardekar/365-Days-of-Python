from collections import deque

def is_valid_move(x, y, n):
    return 0 <= x < n and 0 <= y < n

def min_moves_to_target(n, start_row, start_col, end_row, end_col):
    # Possible moves for the knight
    moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

    # Initialize the chessboard with -1 to mark unvisited squares
    chessboard = [[-1 for _ in range(n)] for _ in range(n)]
    
    # Set the starting position to 0
    chessboard[start_row][start_col] = 0

    # Create a queue for BFS
    queue = deque([(start_row, start_col)])

    while queue:
        current_row, current_col = queue.popleft()

        # Check if we've reached the target position
        if current_row == end_row and current_col == end_col:
            return chessboard[current_row][current_col]

        # Try all possible knight moves
        for move_x, move_y in moves:
            new_row, new_col = current_row + move_x, current_col + move_y

            if is_valid_move(new_row, new_col, n) and chessboard[new_row][new_col] == -1:
                # Mark the new position as visited
                chessboard[new_row][new_col] = chessboard[current_row][current_col] + 1
                queue.append((new_row, new_col))

    # If we can't reach the target position, return -1
    return -1

# Example usage:
# n = 9
# start_row = 4
# start_col = 4
# end_row = 4
# end_col = 8

n = 6
start_row = 5
start_col = 1
end_row = 0
end_col = 5

result = min_moves_to_target(n, start_row, start_col, end_row, end_col)
print("Minimum number of moves:", result)
