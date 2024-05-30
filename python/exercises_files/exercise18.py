############ Score of a String ############

# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

# Return the score of s.

# Example 1:

# Input: s = "hello"
# Output: 13

# Explanation:

# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111.
# So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:

# Input: s = "zaz"
# Output: 50

# Explanation:

# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.


# def scoreOfString(s: str) -> int:
#     example = "Hello"

#     ASCII -> total value of "Hello" = 13
#     "h" = 104 -> i
#     "e" = 101 -> (i+1)
#     "l" = 108 -> (i+2)
#     "l" = 108 -> (i+2)
#     "o" = 111 -> (i+3)

#     |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111|

#     Problem Logic:

#     score_string = abs(i - (i+1)) + abs((i+1) - (i+2)) + abs((i+2) - (i+2)) + abs((i+2) - (i+3))

#     Pseudocode:

#     1. lower string -> check
#     2. loop string -> check
#     3. execute problem logic inside the loop -> check
#     4. build helper function to calculate total ASCII values -> check
#     5. method value for ASCII char -> ord('a')


## Solution 1:
# def charsOperation(char: str, next_char: str):
#     if char == next_char:
#         return ord(char) - ord(char)
#     else:
#         return ord(char) - ord(next_char)


# def scoreOfString(score_string: str) -> int:
#     lower_score_string = score_string.lower()
#     total_sum = 0
#     for i in range(0, len(lower_score_string) - 1):
#         single_score = abs(
#             charsOperation(lower_score_string[i], lower_score_string[i + 1])
#         )
#         total_sum += single_score
#     return total_sum


# score_string_test = "Hello"
# print(scoreOfString(score_string_test))
# score_string_test2 = "zaz"
# print(scoreOfString(score_string_test2))


## Best performance solution:
def scoreOfString(s: str) -> int:
    a = list(s)
    b = [ord(i) for i in a]
    ans = 0
    for i in range(1, len(b)):
        ans += abs(b[i] - b[i - 1])
    return ans
