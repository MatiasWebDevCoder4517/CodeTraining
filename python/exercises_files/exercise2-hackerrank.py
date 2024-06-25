#### look at the exercise2-hackerrank.png image in folder exercises_images ####

## SOLUTION 1
import math
import os
import random
import re
import sys


## Context:

## find the minimum-maximum value of the total sum of 4 integers in a array with len = 55
## print minimum value + <two_spaces> + maximum 

## arr = [1,3,5,7,9]
## sorted_arr = sorted(arr) --> [1,3,5,7,9] --> minimum = 16
## sorted_arr (reverse) = --> [9,7,5,3,1] --> maximum = 24

## Pseudocode:

## sort the array from lowest to highest value
## sort (reverse) the array from highest to lowest value
## sum up both sorted arrays and save them in different variables
## print the variables according to the special condition

## Restrictions:

## len of the array must be 5 items long.
## items of the array must be integers

def miniMaxSum(arr):
    if not (len(arr) == 5):
        raise ValueError("The length of the array must be exactly 5!")
    else:
    
        low_sort_array = sorted(arr)
        ##print(low_sort_array)
        high_sort_array = sorted(arr, reverse=True)
        ##print(high_sort_array)
        minimum_value = 0
        maximum_value = 0
        
        for i in range(0, len(low_sort_array)-1):
            minimum_value += low_sort_array[i]
            
        for j in range(0, len(high_sort_array)-1):
            maximum_value += high_sort_array[j]
        
        print(f"{minimum_value} {maximum_value}")

