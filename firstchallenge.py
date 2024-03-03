def solution(A):
    N = len(A)  # Number of boxes
    total_bricks = sum(A)  # Total number of bricks across all boxes
    desired_total = N * 10  # Desired total number of bricks for equal distribution

    # Check if redistribution to exactly 10 bricks per box is possible
    if total_bricks != desired_total:
        return -1

    # Calculate the minimum number of moves required for redistribution
    moves = 0
    cumulative_diff = 0
    for bricks in A:
        # Calculate the difference for the current box
        diff = bricks - 10
        cumulative_diff += diff
        # Accumulate the absolute value of the cumulative difference
        moves += abs(cumulative_diff)

    return moves
