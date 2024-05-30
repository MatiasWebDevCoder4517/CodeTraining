# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: X

# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output
# The highest score in the class is: 91


def highest_score(scores: list[int]) -> int:
    if not scores:
        return None  # Return None if the list is empty

    highest = scores[0]  # Initialize the highest number with the first element

    for score in scores[1:]:
        if score > highest:
            highest = score

    return highest


# Example list
student_scores_test = [78, 65, 89, 86, 55, 91, 1000, 89, 100, 200, 300]
print(highest_score(student_scores_test))