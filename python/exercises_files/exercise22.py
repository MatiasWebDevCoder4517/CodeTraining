############ Pascal's Triangle ############

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

# Constraints:

# 1 <= numRows <= 30


## PSEUDOCODE ##

# code_logic => investigate Pascal's math formula and translate to python

# Pascal's formula ->

# Exp   |  row
# 11**0 = [1] --> 1 (length = 1)
# 11**1 = [1, 1] --> 11 (length = 2)
# 11**2 = [1, 2, 1] --> 121 (length = 3)
# 11**3 = [1, 3, 3, 1] --> 1331 (length = 4)
# 11**4 = [1, 4, 6, 4, 1] --> 14641 (length = 5)

# 1. create empty result list
# 2. loop the empty result list
# 3. execute code_logic (build helper function??)
# 4. fill the result list


## Solution 1:
import math


def separate_digits(number_string: str) -> list:
    return [int(digit) for digit in number_string]


def execute_pascal_formula(n_row):
    pascal_row = []
    for r in range(n_row + 1):
        binom_coeff = math.factorial(n_row) // (
            math.factorial(r) * math.factorial(n_row - r)
        )
        pascal_row.append(binom_coeff)
    return pascal_row


def generate(numRows: int) -> list[list[int]]:
    final_result_list = []
    for numRow in range(0, numRows):
        pascal_result = execute_pascal_formula(numRow)
        exponent = separate_digits(pascal_result)
        final_result_list.append(exponent)
    return final_result_list


## Best performance approach:
def generate(numRows: int) -> list[list[int]]:
    res = [[1]]

    for _ in range(numRows - 1):
        dummy_row = [0] + res[-1] + [0]
        row = []

        for i in range(len(res[-1]) + 1):
            row.append(dummy_row[i] + dummy_row[i + 1])
        res.append(row)
    return res


numRows_test = 5
print(generate(numRows_test))
