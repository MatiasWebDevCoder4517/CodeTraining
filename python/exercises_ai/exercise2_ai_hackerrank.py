########################### BOT SAVES PRINCESS 2 ###########################


# In this version of "Bot saves princess", Princess Peach and bot's position are randomly set. Can you save the princess?

# Task
# Complete the function nextMove which takes in 4 parameters - an integer N,
# integers r and c indicating the row & column position of the bot and the character array grid - and outputs the next move the bot makes to rescue the princess.

# Input Format
# The first line of the input is N (<100), the size of the board (NxN).
# The second line of the input contains two space separated integers, which is the position of the bot.

# Grid is indexed using Matrix Convention
# The position of the princess is indicated by the character 'p' and the position of the bot is indicated by the character 'm' and each cell is denoted by '-' (ascii value: 45).

# Output Format
# Output only the next move you take to rescue the princess. Valid moves are LEFT, RIGHT, UP or DOWN

# Sample Input
# 5
# 2 3
# -----
# -----
# p--m-
# -----
# -----

# Sample Output
# LEFT

# Resultant State
# -----
# -----
# p-m--
# -----
# -----

# Code sample:

# def nextMove(n,r,c,grid):
#     return ""

# n = int(input())
# r,c = [int(i) for i in input().strip().split()]
# grid = []
# for i in range(0, n):
#     grid.append(input())

# print(nextMove(n,r,c,grid))


## SOLUTION 1
def nextMove(n, r, c, grid):
    # Find the coordinates of the princess
    princess_pos = None

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "p":
                princess_pos = (i, j)
                break

    # Calculate the differences
    row_diff = princess_pos[0] - r
    col_diff = princess_pos[1] - c

    # Determine the next move
    if row_diff < 0:
        return "UP"
    elif row_diff > 0:
        return "DOWN"
    elif col_diff < 0:
        return "LEFT"
    elif col_diff > 0:
        return "RIGHT"


# Sample input processing
n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(n):
    grid.append(input().strip())

print(nextMove(n, r, c, grid))
