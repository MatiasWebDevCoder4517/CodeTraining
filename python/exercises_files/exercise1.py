# Steps to Implement Radix Sort:

# Identify the Maximum Number: Find the maximum number in the array to know the number of digits.
# Counting Sort for Each Digit: Use a modified counting sort for each digit. Unlike a typical counting sort that sorts elements based on the keys themselves,
# here the sorting is done based on the individual digits.


## Solution 1:
def countingSort(array, digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10

    digitColumn = 10**digit
    for num in array:
        countIndex = (num // digitColumn) % 10
        countArray[countIndex] += 1

    for index in range(1, 10):
        countArray[index] += countArray[index - 1]

    for index in range(len(array) - 1, -1, -1):
        countIndex = (array[index] // digitColumn) % 10
        countArray[countIndex] -= 1
        sortedIndex = countArray[countIndex]
        sortedArray[sortedIndex] = array[index]

    for index in range(len(array)):
        array[index] = sortedArray[index]


def radixSort(array):
    if len(array) == 0:
        return array

    maxNumber = max(array)
    digit = 0
    while maxNumber / 10**digit > 0:
        countingSort(array, digit)
        digit += 1
    return array

 ########################################################################################

## Solution 2:
def counting_sort_by_digit(array, digit_place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # count occurrences of each digit
    for index in range(size):
        index = array[index] // digit_place
        count[index % 10] += 1

    # cumulative count
    for index in range(1, 10):
        count[index] += count[index - 1]

    # build the output array using count
    index = size - 1
    while index >= 0:
        result_index = array[index] // digit_place
        output[count[result_index % 10] - 1] = array[index]
        count[result_index % 10] -= 1
        index -= 1

    for index in range(size):
        array[index] = output[index]


def radixSort(array):
    max_num = max(array)

    digit_place = 1
    while max_num // digit_place > 0:
        counting_sort_by_digit(array, digit_place)
        digit_place *= 10
    return array
