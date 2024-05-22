############ Widest Vertical Area Between Two Points Containing No Points ############


# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
# The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.

# Example 1:
# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.

# Example 2:
# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3

# Constraints:

# n == points.length
# 2 <= n <= 105
# points[i].length == 2
# 0 <= xi, yi <= 109


## Solution 1:
def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    x_cords = sorted(point[0] for point in points)
    max_width = 0
    for index in range(1, len(x_cords)):
        gap = x_cords[index] - x_cords[index - 1]
        if gap > max_width:
            max_width = gap
    return max_width


## Solution 2:
def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    points.sort()
    diff = 0
    for i in range(1, len(points)):
        diff = max(diff, points[i][0] - points[i - 1][0])
    return diff


# Example usage:
points1 = [[8, 7], [9, 9], [7, 4], [9, 7]]
print(maxWidthOfVerticalArea(points1))  # Output: 1

points2 = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
print(maxWidthOfVerticalArea(points2))  # Output: 3
