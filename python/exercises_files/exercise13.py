############ Merge Strings Alternately ############

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d


# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


## Solution 1:
# def mergeAlternately(word1, word2):
#     # Determine the length of the shorter string
#     min_length = min(len(word1), len(word2))

#     # Initialize the result string
#     result = []

#     # Alternate the characters from both strings
#     for i in range(min_length):
#         result.append(word1[i])
#         result.append(word2[i])

#     # Append the remaining characters from the longer string
#     result.append(word1[min_length:])  # Remaining part of word1 if any
#     result.append(word2[min_length:])  # Remaining part of word2 if any

#     # Join the list of characters into a string and return
#     return "".join(result)


## Solution 2:
def mergeAlternately(word1: str, word2: str) -> str:
    mergeString = ""
    i = 0
    j = 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            mergeString = mergeString + word1[i]
            i += 1

        if j < len(word2):
            mergeString = mergeString + word2[j]
            j += 1
    return mergeString

# Example usage:
print(mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
print(mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
print(mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
