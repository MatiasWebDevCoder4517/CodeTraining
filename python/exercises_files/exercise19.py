############ Modify Columns ############

# DataFrame employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | salary      | int    |
# +-------------+--------+
# A company intends to give its employees a pay rise.

# Write a solution to modify the salary column by multiplying each salary by 2.

# The result format is in the following example.

# Example 1:

# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 19666  |
# | Piper   | 74754  |
# | Mia     | 62509  |
# | Ulysses | 54866  |
# +---------+--------+

# Output:
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
# +---------+--------+

# Explanation:
# Every salary has been doubled.

## PSEUDOCODE ##
# import pandas as pd

# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:

#     code_logic => rised_salary = value(i) * 2

#     helper_function:

#     1.1 -> if a value is negative, skip it and say it, otherwise apply code_logic

#     1. capture whole 'salary' column with its values -> check
#     2. loop each value to the last one -> check
#     3. apply code logic (build helper function?) -> check
#     4. modify original = value(i) with the new_value = rised_salary
#     5. return the new dataframe with the all rised_values


## Solution 1:
import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary *= 2
    return employees
