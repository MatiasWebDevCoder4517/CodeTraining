########################### BOTCLEAN ###########################


# The goal of Artificial Intelligence is to create a rational agent (Artificial Intelligence 1.1.4).
# An agent gets input from the environment through sensors and acts on the environment with actuators.
# In this challenge, you will program a simple bot to perform the correct actions based on environmental input.

# Meet the bot MarkZoid. It's a cleaning bot whose sensor is a head mounted camera and whose actuators are the wheels beneath it.
# It's used to clean the floor.

# The bot here is positioned at the top left corner of a 5*5 grid.
# Your task is to move the bot to clean all the dirty cells.

# Input Format

# The first line contains two space separated integers which indicate the current position of the bot.
# The board is indexed using Matrix Convention
# 5 lines follow representing the grid.
# Each cell in the grid is represented by any of the following 3 characters:
#     'b' (ascii value 98) indicates the bot's current position, 'd' (ascii value 100) indicates a dirty cell and '-' (ascii value 45) indicates a clean cell in the grid.

# Note If the bot is on a dirty cell, the cell will still have 'd' on it.

# Output Format
# The output is the action that is taken by the bot in the current step,
# and it can be either one of the movements in 4 directions or cleaning up the cell in which it is currently located.
# The valid output strings are LEFT, RIGHT, UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell.
# Repeat this process until all the cells on the grid are cleaned.

# Sample Input #00
# 0 0
# b---d
# -d--d
# --dd-
# --d--
# ----d

# Sample Output #00
# RIGHT

# Resultant state
# -b--d
# -d--d
# --dd-
# --d--
# ----d

# Sample Input #01
# 0 1
# -b--d
# -d--d
# --dd-
# --d--
# ----d

# Sample Output #01
# DOWN

# Resultant state
# ----d
# -d--d
# --dd-
# --d--
# ----d

# Task
# Complete the function next_move that takes in 3 parameters posr, posc being the co-ordinates of
# the bot's current position and board which indicates the board state to print the bot's next move.
# The codechecker will keep calling the function next_move till the game is over or you make an invalid move.

## Code Sample:

# Head ends here

# def next_move(posr, posc, board):
#     print("")

# # Tail starts here

# if __name__ == "__main__":
#     pos = [int(i) for i in input().strip().split()]
#     board = [[j for j in input().strip()] for i in range(5)]
#     next_move(pos[0], pos[1], board)


## SOLUTION 1 (wrong):
# def next_move(posr, posc, board):
#     # Find the coordinates of all dirty cells
#     dirty_cells = []
#     for i in range(5):
#         for j in range(5):
#             if board[i][j] == "d":
#                 dirty_cells.append((i, j))

#     # Find the closest dirty cell
#     closest_dirty_cell = None
#     min_distance = float("inf")

#     for cell in dirty_cells:
#         distance = abs(posr - cell[0]) + abs(posc - cell[1])
#         if distance < min_distance:
#             min_distance = distance
#             closest_dirty_cell = cell

#     # Determine the next move
#     if closest_dirty_cell:
#         if posr > closest_dirty_cell[0]:
#             return "UP"
#         elif posr < closest_dirty_cell[0]:
#             return "DOWN"
#         elif posc > closest_dirty_cell[1]:
#             return "LEFT"
#         elif posc < closest_dirty_cell[1]:
#             return "RIGHT"
#     else:
#         return "CLEAN"


# # Tail starts here
# if __name__ == "__main__":
#     pos = [int(i) for i in input().strip().split()]
#     board = [[j for j in input().strip()] for _ in range(5)]
#     print(next_move(pos[0], pos[1], board))


## SOLUTION 2:
import math


# Update cost that bot need to arrive the dirty
def update_position(posr, posc, dirties):
    nearest_dirt = []
    for i in range(len(dirties)):
        # Euclidean distance
        result = math.sqrt(
            ((dirties[i][0] - posr) ** 2) + ((dirties[i][1] - posc) ** 2)
        )
        nearest_dirt.append(result)
    return [x for (y, x) in sorted(zip(nearest_dirt, dirties))]


# Set the bot in your new position
def next_move(posr, posc, board):
    dirties = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "d":
                dirties.append([i, j])

    next_dirt = update_position(posr, posc, dirties)
    if next_dirt[0][1] < posc:
        print("LEFT")
    elif next_dirt[0][1] > posc:
        print("RIGHT")
    elif next_dirt[0][0] < posr:
        print("UP")
    elif next_dirt[0][0] > posr:
        print("DOWN")
    else:
        print("CLEAN")


# Set the data
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
