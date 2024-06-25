#!/usr/bin/python

########################### BOT SAVES PRINCESS ###########################

#### look at the exercise1_ai_hackerrank.png image in folder exercises_images ####

## SOLUTION 1:
def displayPathtoPrincess(n, grid):
    # Find the coordinates of 'm' and 'p'
    bot_pos = None
    princess_pos = None

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "m":
                bot_pos = (i, j)
            elif grid[i][j] == "p":
                princess_pos = (i, j)

    # Calculate row and column differences
    row_diff = princess_pos[0] - bot_pos[0]
    col_diff = princess_pos[1] - bot_pos[1]

    # Print the moves
    if row_diff < 0:
        print("UP\n" * abs(row_diff), end="")
    elif row_diff > 0:
        print("DOWN\n" * abs(row_diff), end="")

    if col_diff < 0:
        print("LEFT\n" * abs(col_diff), end="")
    elif col_diff > 0:
        print("RIGHT\n" * abs(col_diff), end="")


m = int(input("Print the moves: "))
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
