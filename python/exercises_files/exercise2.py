# Overview of Merge Sort

# Merge Sort works by:

# Dividing the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
# Repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

# Steps to Implement Merge Sort
# The implementation involves two main functions:

# merge_sort Function: This function recursively splits the array into halves until the sub-arrays have only one element each.
# merge Function: This function takes two sorted sub-arrays and merges them into a single sorted array.

# Detailed Implementation Steps:

# Splitting the Array:
# If the array has more than one element, split the array into two halves.
# Recursively sort each half.

# Merging the Arrays:
# Compare the elements at the beginnings of both halves.
# Add the smaller element to the result array and move the index in that half forward.
# Continue until all elements in both halves are added to the result.
# Ensure any remaining elements from either half are added to the end of the result array.


## Solution 1:
def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k_index = i_index = j_index = 0
    while i_index < len(leftHalf) and j_index < len(rightHalf):
        if leftHalf[i_index] <= rightHalf[j_index]:
            sortedArray[k_index] = leftHalf[i_index]
            i_index += 1
        else:
            sortedArray[k_index] = rightHalf[j_index]
            j_index += 1
        k_index += 1
    while i_index < len(leftHalf):
        sortedArray[k_index] = leftHalf[i_index]
        i_index += 1
        k_index += 1
    while j_index < len(rightHalf):
        sortedArray[k_index] = rightHalf[j_index]
        j_index += 1
        k_index += 1
    return sortedArray


def mergeSort(array):
    if len(array) == 1:
        return array
    middleIndex = len(array) // 2
    leftHalf = array[:middleIndex]
    rightHalf = array[middleIndex:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


########


## Solution 2:
def doMerge(mainArray, startindex, middleindex, endindex, aux_array):
    k_index = startindex
    i_index = startindex
    j_index = middleindex + 1
    while i_index <= middleindex and j_index <= endindex:
        if aux_array[i_index] <= aux_array[j_index]:
            mainArray[k_index] = aux_array[i_index]
            i_index += 1
        else:
            mainArray[k_index] = aux_array[j_index]
            j_index += 1
        k_index += 1
    while i_index <= middleindex:
        mainArray[k_index] = aux_array[i_index]
        i_index += 1
        k_index += 1
    while j_index <= endindex:
        mainArray[k_index] = aux_array[j_index]
        j_index += 1
        k_index += 1


def mergeSortHelper(mainArray, startindex, endindex, aux_array):
    if startindex == endindex:
        return
    middleindex = (startindex + endindex) // 2
    mergeSortHelper(aux_array, startindex, middleindex, mainArray)
    mergeSortHelper(aux_array, middleindex + 1, endindex, mainArray)
    doMerge(mainArray, startindex, middleindex, endindex, aux_array)


def mergeSort(array):
    if len(array) <= 1:
        return array
    aux_array = array[:]
    mergeSortHelper(array, 0, len(array) - 1, aux_array)
    return array


########


## Solution 3:
def mergeArray(left, right):
    sorted_array = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1

        else:
            sorted_array.append(right[right_index])
            right_index += 1

    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    return sorted_array


def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = mergeSort(array[:mid])
    right_half = mergeSort(array[mid:])
    return mergeArray(left_half, right_half)


########

# Example usage
array = [8, 5, 2, 9, 5, 6, 3]
sorted_array = paste_function(array)
print(sorted_array)
