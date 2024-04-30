#### look at the exercise5.png image in folder exercises_images


## Solution 1:
def maximizeExpression(array):
    if len(array) < 4:
        return 0

    maxofA = [array[0]]
    maxofAminusB = [float("-inf")]
    maxofAminusBplusC = [float("-inf")] * 2
    maxofAminusBplusCminusD = [float("-inf")] * 3

    for index in range(1, len(array)):
        currentMax = max(maxofA[index - 1], array[index])
        maxofA.append(currentMax)

    for index in range(1, len(array)):
        currentMax = max(maxofAminusB[index - 1], maxofA[index - 1] - array[index])
        maxofAminusB.append(currentMax)

    for index in range(2, len(array)):
        currentMax = max(
            maxofAminusBplusC[index - 1], maxofAminusB[index - 1] + array[index]
        )
        maxofAminusBplusC.append(currentMax)

    for index in range(3, len(array)):
        currentMax = max(
            maxofAminusBplusCminusD[index - 1],
            maxofAminusBplusC[index - 1] - array[index],
        )
        maxofAminusBplusCminusD.append(currentMax)
    return maxofAminusBplusCminusD[len(maxofAminusBplusCminusD) - 1]


## Solution 2:
def maximizeExpression(array):
    if len(array) < 4:
        return 0

    max_a = array[0]
    max_ab = float("-inf")
    max_abc = float("-inf")
    max_abcd = float("-inf")

    for i_index in range(1, len(array)):
        if i_index >= 3:  # possible d
            max_abcd = max(max_abcd, max_abc - array[i_index])
        if i_index >= 2:  # possible c
            max_abc = max(max_abc, max_ab + array[i_index])
        if i_index >= 1:  # possible b
            max_ab = max(max_ab, max_a - array[i_index])

        # Update max_a for possible future a's
        max_a = max(max_a, array[i_index])
    return max_abcd


# Example usage
array = [3, 6, 1, -3, 2, 7]
print(paste_solution_function(array))  # Outputs: 4
