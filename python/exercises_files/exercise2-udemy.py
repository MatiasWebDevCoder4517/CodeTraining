# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# Write a program that converts their scores to grades. By the end of your program,
# you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

# The final version of the student_grades dictionary will be checked.

# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

# Hints:
# Remember that looping through a Dictionary will only give you the keys and not the values.
# If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.
# At the end of your program, the print statement will show the final student_scores dictionary, do not change this.


## naive approach
def get_grades_naive(student_scores: dict) -> dict:
    grades = {
        "Outstanding": 90,
        "Exceeds Expectations": 80,
        "Acceptable": 70,
        "Fail": 60,
    }
    grade_keys = list(grades.keys())
    for student, score in student_scores.items():
        if score >= 90:
            student_scores[student] = grade_keys[0]
        elif score > 80:
            student_scores[student] = grade_keys[1]
        elif score > 70:
            student_scores[student] = grade_keys[2]
        elif score > 60:
            student_scores[student] = grade_keys[3]
        else:
            student_scores[student] = "Fail"  # Handle scores below 60 if needed
    return student_scores


## using match and cases approach:
def get_grades_naive_matches(student_scores: dict) -> dict:
    grades = {
        "Outstanding": 90,
        "Exceeds Expectations": 80,
        "Acceptable": 70,
        "Fail": 60,
    }
    grade_keys = list(grades.keys())
    for student, score in student_scores.items():
        match score:
            case _ if score >= 90:
                student_scores[student] = grade_keys[0]
            case _ if score > 80:
                student_scores[student] = grade_keys[1]
            case _ if score > 70:
                student_scores[student] = grade_keys[2]
            case _ if score > 60:
                student_scores[student] = grade_keys[3]
            case _:
                student_scores[student] = "Fail"  # Handle scores below 60 if needed
    return student_scores


## efficient approach
from bisect import bisect_right


def get_grades_bisect(student_scores: dict) -> dict:
    grades = {
        "Outstanding": 90,
        "Exceeds Expectations": 80,
        "Acceptable": 70,
        "Fail": 60,
    }

    thresholds = sorted(grades.values(), reverse=True)
    grade_labels = [k for k in sorted(grades, key=grades.get, reverse=True)]

    for student, score in student_scores.items():
        index = bisect_right(thresholds, score)
        student_scores[student] = (
            grade_labels[index] if index < len(grade_labels) else "Fail"
        )
    return student_scores


## testing performance and time execution:
import timeit

student_scores_test = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


def wrapper_get_grades_naive():
    return get_grades_naive(student_scores_test.copy())


def wrapper_get_grades_bisect():
    return get_grades_bisect(student_scores_test.copy())


def wrapper_get_grades_matches():
    return get_grades_naive_matches(student_scores_test.copy())


# Measure execution time
naive_time = timeit.timeit(wrapper_get_grades_naive, number=10000)
bisect_time = timeit.timeit(wrapper_get_grades_bisect, number=10000)
naive_matches_time = timeit.timeit(wrapper_get_grades_matches, number=10000)

print(f"Naive loop function time: {naive_time:.6f} seconds")
print(f"Bisect function time: {bisect_time:.6f} seconds")
print(f"naive matches function time: {naive_matches_time:.6f} seconds")
