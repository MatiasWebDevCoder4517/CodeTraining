############ Find the Maximum Achievable Number ############


# Given two integers, num and t. A number is achievable if it can become equal to num after applying the following operation:

# Increase or decrease the number by 1, and simultaneously increase or decrease num by 1.
# Return the maximum achievable number after applying the operation at most t times.

# Example 1:

# Input: num = 4, t = 1
# Output: 6

# Explanation:

# Apply the following operation once to make the maximum achievable number equal to num:
# Decrease the maximum achievable number by 1, and increase num by 1.

# Example 2:

# Input: num = 3, t = 2
# Output: 7

# Explanation:

# Apply the following operation twice to make the maximum achievable number equal to num:
# Decrease the maximum achievable number by 1, and increase num by 1.

# Constraints:
# 1 <= num, t <= 50


## PSEUDOCODE ##

# code_logic => max_achievable = num + 2 or num + (-2)

# if not max_achievable:
#     return "Error invalid num"

# if num <= max_achievable:
#     continue
# else:
#     return max_achievable


# 0. loop t var -> check
# 1. cases = (4 + 1) + 1 = 6 | (4 - 1) + 1 = 4 | (4 + 1) - 1 = 4 | (4 - 1) - 1 = 3
# 2. ONLY max num_achievable
# 3. ONLY possible cases exists where operators are equal.
# 4. Execute code_logic (build helper function?)

# example 1: num = 4, t=2

# t.1:
# cases = (4 + 1) + 1 = 6 | (4 - 1) + 1 = 4 | (4 + 1) - 1 = 4 | (4 - 1) - 1 = 2
# max_num_achievable = 6

# t.2:
# cases = (6 + 1) + 1 = 8 | (6 - 1) + 1 = 6 | (6 + 1) - 1 = 6 | (6 - 1) - 1 = 4
# max_num_achievable = 8

# example 2: num = 3, t=2

# t.1:
# cases = (3 + 1) + 1 = 5 | (3 - 1) + 1 = 3 | (3 + 1) - 1 = 3 | (3 - 1) - 1 = 1
# max_num_achievable = 5

# t.2:
# cases = (5 + 1) + 1 = 7 | (5 - 1) + 1 = 5 | (5 + 1) - 1 = 5 | (5 - 1) - 1 = 3
# max_num_achievable = 7

# example 3: num = 0, t=2

# t.1:
# cases = (0 + 1) + 1 = 2 | (0 - 1) + 1 = 0 | (0 + 1) - 1 = 0 | (0 - 1) - 1 = -2
# max_num_achievable = 2

# t.2:
# cases = (2 + 1) + 1 = 3 | (2 - 1) + 1 = 2 | (2 + 1) - 1 = 2 | (2 - 1) - 1 = 1
# max_num_achievable = 3

# example 4: num = -2, t=2

# t.1:
# cases = (-2 + 1) + 1 = 0 | (-2 - 1) + 1 = -2 | (-2 + 1) - 1 = -2 | (-2 - 1) - 1 = -4
# max_num_achievable = 0

# t.2:
# cases = (0 + 1) + 1 = 2 | (0 - 1) + 1 = 0 | (0 + 1) - 1 = 0 | (0 - 1) - 1 = -2
# max_num_achievable = 2


## Solution 1:
def theMaximumAchievableX(num: int, t: int) -> int:
    return num + 2 * t


num_test = 4
t_test = 2
print(theMaximumAchievableX(num_test, t_test))
