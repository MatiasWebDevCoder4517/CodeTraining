######################## Two Sum ########################

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


## PSEUDOCODE

## start empty dict ==> CHECK
## build 1st condition -> complement = target - num
## iterate the int_list
## build 2nd condition -> if complement in indexed

## * restrictions *
## list must be array of only integers
## target_value must be integer
## list must at least have 1 value


## SOLUTION
def get_two_sum_pairs(int_array: list[int], target_num: int) -> list[int]:
    ## start empty list
    indexed = {}
    ## iterate the int_list
    for i, number in enumerate(int_array):
        complement = target_num - number
        if complement in indexed:
            return [indexed[complement], i]
        indexed[number] = i


test_array_ints = [2, 7, 11, 15]
test_target_num = 18
print(get_two_sum_pairs(test_array_ints, test_target_num))
