#### look at the exercise16.png image in folder exercises_images ####


## Solution 1:
def createSumMatrix(matrix):
    sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    for index in range(1, len(matrix[0])):
        sums[0][index] = sums[0][index - 1] + matrix[0][index]

    for index in range(1, len(matrix)):
        sums[index][0] = sums[index - 1][0] + matrix[index][0]

    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[row])):
            sums[row][column] = (
                sums[row - 1][column]
                + sums[row][column - 1]
                - sums[row - 1][column - 1]
                + matrix[row][column]
            )
    return sums


def maximumSumSubmatrix(matrix, size):
    sums = createSumMatrix(matrix)
    maxSubMatrixSum = float("-inf")

    for row in range(size - 1, len(matrix)):
        for column in range(size - 1, len(matrix[row])):
            total = sums[row][column]

            touches_top_border = row - size < 0
            if not touches_top_border:
                total -= sums[row - size][column]

            touches_left_border = column - size < 0
            if not touches_left_border:
                total -= sums[row][column - size]

            touches_top_or_left_border = touches_top_border or touches_left_border
            if not touches_top_or_left_border:
                total += sums[row - size][column - size]

            maxSubMatrixSum = max(maxSubMatrixSum, total)
    return maxSubMatrixSum


## Solution 2:
def maximumSumSubmatrix(matrix, size):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float("-inf")

    # Iterate over each possible starting point for the size x size submatrix
    for row in range(rows - size + 1):
        for col in range(cols - size + 1):
            current_sum = 0
            # Sum up the elements in the submatrix starting at (row, col)
            for i in range(size):
                for j in range(size):
                    current_sum += matrix[row + i][col + j]

            # Update max_sum if the current_sum of this submatrix is larger
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


# Testing:
matrix = [[5, 3, -18, 10], [14, 12, -78, 88], [6, 45, -23, 8], [7, 23, -1, 4]]
size = 2
print(maximumSumSubmatrix(matrix, size))  # Example output
