# Problem Explanation:

# The task is to determine the length of the longest substring where the number of '(' and ')' are equal, and they are correctly ordered.

# Approach to Solve the Problem:

# Using a Stack:

# Utilize a stack to track indices of unmatched parentheses.
# As you scan the string from left to right:
# If you encounter '(', push its index onto the stack.
# If you encounter ')':
# Pop the top of the stack (this matches the most recent unmatched '(').
# Calculate the length of the current balanced substring by subtracting the current index from the top index of the stack.
# If the stack is empty after popping, push the current index onto the stack (it becomes the new base for future matches).

# Without Extra Space (Optimized Two-Pass Method):

# Perform two passes over the string:

# First Pass (left to right):
# Increment a counter for '(', decrement for ')'.
# If the counter becomes zero, update the result to the current length.
# If the counter goes negative (more ')' than '('), reset the counter.

# Second Pass (right to left):
# Reset and repeat the process considering ')' as the starting point.
# This catches imbalances starting with excess '(' from the end of the string.


## Solution 1:
def longestBalancedSubstring(string):
    maxLength = 0
    indexStack = []
    indexStack.append(-1)

    for index in range(len(string)):
        if string[index] == "(":
            indexStack.append(index)
        else:
            indexStack.pop()
            if len(indexStack) == 0:
                indexStack.append(index)
            else:
                balancedSubStringStartindex = indexStack[len(indexStack) - 1]
                currentLength = index - balancedSubStringStartindex
                maxLength = max(maxLength, currentLength)
    return maxLength


## Solution 2:
def longestBalancedSubstring(string):
    maxLength = 0
    openingCount = 0
    closingCount = 0

    for char in string:
        if char == "(":
            openingCount += 1
        else:
            closingCount += 1
        if openingCount == closingCount:
            maxLength = max(maxLength, closingCount * 2)
        elif closingCount > openingCount:
            openingCount = 0
            closingCount = 0

    openingCount = 0
    closingCount = 0
    for index in reversed(range(len(string))):
        char = string[index]
        if char == "(":
            openingCount += 1
        else:
            closingCount += 1
        if openingCount == closingCount:
            maxLength = max(maxLength, openingCount * 2)
        elif openingCount > closingCount:
            openingCount = 0
            closingCount = 0
    return maxLength


## Solution 3:
def longestBalancedSubstring(string):
    max_length = 0
    left = right = 0

    # left to right
    for char in string:
        if char == "(":
            left += 1
        else:
            right += 1

        if left == right:
            max_length = max(max_length, 2 * right)
        elif right > left:
            left = right = 0

    # right to left
    left = right = 0
    for char in reversed(string):
        if char == ")":
            right += 1
        else:
            left += 1

        if left == right:
            max_length = max(max_length, 2 * left)
        elif left > right:
            left = right = 0
    return max_length


## Solution 4:
def getLongestBalancedInDirection(string, leftToRight):
    openingParens = "(" if leftToRight else ")"
    startindex = 0 if leftToRight else len(string) - 1
    step = 1 if leftToRight else -1

    maxLength = 0
    openingCount = 0
    closingCount = 0

    index = startindex
    while index >= 0 and index < len(string):
        char = string[index]

        if char == openingParens:
            openingCount += 1
        else:
            closingCount += 1

        if openingCount == closingCount:
            maxLength = max(maxLength, closingCount * 2)
        elif closingCount > openingCount:
            openingCount = 0
            closingCount = 0

        index += step
    return maxLength


def longestBalancedSubstring(string):
    return max(
        getLongestBalancedInDirection(string, True),
        getLongestBalancedInDirection(string, False),
    )


# Example usage
string = "(()))"
print(paste_solution_function(string))
