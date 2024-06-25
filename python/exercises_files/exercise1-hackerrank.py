#!/bin/python3


#### look at the exercise1-hackerrank.png image in folder exercises_images ####


import math
import os
import random
import re
import sys

## Code Context:

## count positives items, negative items and zero items (as number)
## Divide each total count with the len of the array
## print the "ratio" of each divition

## Pseudocode:

## save length of the array in a variable
## iterate the array
## 1st condition -> determine if index have positive symbol or negative symbol or non-symbol (zero)
## 2nd condition -> on each determination of the symbol, save a total count.
## (Inititate 3 different variables before)
## After loop ends, obtain the ratio of the items (total_count/len(arr))
## print the results with separte lines (\n)

## helper function??.

## symbol determination, return a single symbol output

## Capture symbol:

## For positives: item >= 1
## For negatives: item < 0
## For zeroes: item == 0


def get_symbol(num: int) -> str:
    ## 1st condition -> determine if index have positive symbol or negative symbol or non-symbol (zero)
    if num >= 1:
        ##print("Number has positive symbol")
        symbol = "+"
    elif num < 0:
        ##print("Number has negative symbol")
        symbol = "-"
    elif num == 0:
        ##print("Number is zero!")
        symbol = ""
    else:
        return None
    return symbol


def plusMinus(arr: list) -> float | None:
    ## save length of the array in a variable
    arr_length = len(arr)
    total_positives = 0
    total_negatives = 0
    total_zeroes = 0
    positives_ratio = 0.0
    negatives_ratio = 0.0
    zeroes_ratio = 0.0

    ## iterate the array
    for i in arr:
        ##print(i)
        symbol = get_symbol(i)
        ## 2nd condition -> on each determination of the symbol, save a total count.
        if symbol == "+":
            total_positives += 1
        elif symbol == "-":
            total_negatives += 1
        if symbol == "":
            total_zeroes += 1

    ## After loop ends, obtain the ratio of the items (total_count/len(arr))
    positives_ratio = total_positives / arr_length
    negatives_ratio = total_negatives / arr_length
    zeroes_ratio = total_zeroes / arr_length

    ## print the results with separte lines (\n)
    return f"{positives_ratio:.6f}, {negatives_ratio:.6f}, {zeroes_ratio:.6f}"


test_array = [1, 1, 0, -1, -1]
print(plusMinus(test_array))
