############ Greatest Common Divisor of Strings ############

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


## Solution 1:
def gcdOfStrings(str1, str2):
    # If both strings are identical, the GCD string is either of them
    if str1 == str2:
        return str1

    # Ensure str1 is always the longer string
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    # Check if the longer string starts with the shorter string
    if not str1.startswith(str2):
        return ""

    # Apply the Euclidean algorithm by subtracting the common prefix and recurse
    return gcdOfStrings(str1[len(str2) :], str2)


## Solution 2:
def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""

    if len(str1) == len(str2):
        return str1

    if len(str1) > len(str2):
        return gcdOfStrings(str1[len(str2) :], str2)
    
    return gcdOfStrings(str1, str2[len(str1) :])


# Example usage:
print(gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(gcdOfStrings("LEET", "CODE"))  # Output: ""
