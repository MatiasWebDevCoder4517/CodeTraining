############ Counting Bits ############

# Given an integer 'n', return an array 'ans' of length 'n + 1' such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]

# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]

# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# Constraints:
# 0 <= n <= 105

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


## PSEUDOCODE ##
##code_logic => bin(number)[2:]  # Remove the '0b' prefix


# 1. n to list
# 2. len of the list must be n + 1 limit
# 3. loop the list
# 3. execute code_logic
# 4.


## Solution 1:
# def get_binary_using_bin(number: int) -> str:
#     return bin(number)[2:]  # Remove the '0b' prefix


# def count_ones(binary_string: str) -> int:
#     return binary_string.count("1")


# def countBits(n: int) -> list[int]:
#     final_binary_list = []
#     for i in range(0, n + 1):
#         binary_num = get_binary_using_bin(i)
#         total_ones = count_ones(binary_num)
#         final_binary_list.append(total_ones)
#     return final_binary_list


## Best performance solution:
def countBits(n: int) -> list[int]:
    dp = [0, 1]
    while len(dp) <= n:
        dp = dp + [1 + x for x in dp]
    return dp[: n + 1]


binary_num_test = 5
print(countBits(binary_num_test))
