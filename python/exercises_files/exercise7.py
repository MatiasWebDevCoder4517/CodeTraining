#### look at the exercise7.png image in folder exercises_images


## Solution:
def transposeMatrix(matrix):
    # Row count and column count in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Prepare the transposed matrix with empty lists for each new row (originally columns)
    transposed = [[] for _ in range(cols)]

    # Fill the transposed matrix
    for i in range(cols):
        for j in range(rows):
            transposed[i].append(matrix[j][i])
    return transposed


## Solution 2:
def transposeMatrix(matrix):
    transposed_matrix = []
    for column in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][column])
        transposed_matrix.append(new_row)
    return transposed_matrix
