# Objective:
# Identify the smallest substring in the big string which contains all the characters from the small string, including duplicates.

# Strategy:
# Use a sliding window technique coupled with hash maps to keep track of character frequencies and check for substring completeness.

# Steps to Implement:

# Frequency Count of Small String:
# Create a hash map to count the frequency of each character in the small string.

# Sliding Window Technique:
# Initialize two pointers (start and end) at the start of the big string.
# Use another hash map to track the characters of the big string within the window defined by start and end.
# Expand the end pointer to include new characters until the window has all the characters from the small string.

# Shrink the Window:
# Once the window has all the required characters, attempt to move the start pointer to the right as far as possible while still maintaining a valid window.
# Keep track of the minimum window size and its starting index.

# Result Extraction:
# Use the recorded starting index and minimum size to extract and return the smallest substring.


## Solution 1:
def getCloserBounds(index1, index2, index3, index4):
    return [index1, index2] if index2 - index1 < index4 - index3 else [index3, index4]


def getStringFromBounds(string, bounds):
    start, end = bounds
    if end == float("inf"):
        return ""
    return string[start : end + 1]


def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1


def decreaseCharCount(char, charCounts):
    charCounts[char] -= 1


def getCharCounts(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts


def getSubstringBounds(string, targetCharCounts):
    substringBounds = [0, float("inf")]
    substringCharCounts = {}
    numUniqueChars = len(targetCharCounts.keys())
    numUniqueCharsDone = 0
    leftindex = 0
    rightindex = 0

    while rightindex < len(string):
        rightChar = string[rightindex]
        if rightChar not in targetCharCounts:
            rightindex += 1
            continue
        increaseCharCount(rightChar, substringCharCounts)
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numUniqueCharsDone += 1

        while numUniqueCharsDone == numUniqueChars and leftindex <= rightindex:
            substringBounds = getCloserBounds(
                leftindex, rightindex, substringBounds[0], substringBounds[1]
            )
            leftChar = string[leftindex]
            if leftChar not in targetCharCounts:
                leftindex += 1
                continue
            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numUniqueCharsDone -= 1
            decreaseCharCount(leftChar, substringCharCounts)
            leftindex += 1
        rightindex += 1
    return substringBounds


def smallestSubstringContaining(bigString, smallString):
    targetCharCounts = getCharCounts(smallString)
    substringBounds = getSubstringBounds(bigString, targetCharCounts)
    return getStringFromBounds(bigString, substringBounds)


## Solution 2:
def smallest_substring_containing(big_string, small_string):
    from collections import Counter

    if not small_string or not big_string:
        return ""

    # Character requirement (frequency of characters in small string)
    char_requirement = Counter(small_string)
    required_chars = len(char_requirement)
    formed_chars = 0
    window_counts = {}

    # Sliding window
    l, r = 0, 0
    min_length = float("inf")
    min_window = ""

    while r < len(big_string):
        character = big_string[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # Check if the current character added is a part of the requirement
        if (
            character in char_requirement
            and window_counts[character] == char_requirement[character]
        ):
            formed_chars += 1

        # Try and contract the window till the point it ceases to be 'desirable'
        while l <= r and formed_chars == required_chars:
            character = big_string[l]

            # Save the smallest window until now
            if r - l + 1 < min_length:
                min_length = r - l + 1
                min_window = big_string[l : r + 1]

            # The character at the position pointed by `l` is no longer a part of the window
            window_counts[character] -= 1
            if (
                character in char_requirement
                and window_counts[character] < char_requirement[character]
            ):
                formed_chars -= 1
            l += 1
        r += 1
    return min_window


# Example usage
big_string = "abcd$ef$axb$c$"
small_string = "$$abf"
print(paste_solution_function(big_string, small_string))
