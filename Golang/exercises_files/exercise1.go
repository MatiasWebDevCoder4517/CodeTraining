// The exercise involves writing a function in Go that identifies the pair of numbers (one from each of two given non-empty arrays)
// which has the smallest absolute difference. The absolute difference is defined as the non-negative difference between two values.
// The result should return these two numbers, with the number from the first array listed first.

// Steps to Solve the Problem:

// Sort Both Arrays:
// Sorting both arrays will make it easier to find the smallest difference by linearly comparing the closest numbers.

// Use Two Pointers:
// Initialize two pointers, one for each array. These will track the current numbers being compared.

// Compare and Update:
// Compare the elements at the current pointers in the two arrays.
// Move the pointer pointing to the smaller element to the next position to find a potentially closer match.
// Track the Smallest Difference: Keep track of the smallest difference and the pair of numbers that produce this difference as you iterate.

package main

import (
	//"log"
	"math"
	"sort"
)

func SmallestDifference(array1, array2 []int) []int {
	sort.Ints(array1)
	sort.Ints(array2)
	index_one, index_two := 0, 0
	smallest, current := math.MaxInt32, math.MaxInt32
	smallest_pair := []int{}
	for index_one < len(array1) && index_two < len(array2) {
		first, second := array1[index_one], array2[index_two]
		if first < second {
			current = second - first
			index_one += 1
		} else if second < first {
			current = first - second
			index_two += 1
		} else {
			return []int{first, second}
		}
		if smallest > current {
			smallest = current
			smallest_pair = []int{first, second}
		}
	}
	return smallest_pair
}

// UNBLOCK FOR TEST
// func main() {
// 	array1_test := []int{-1, 5, 10, 20, 28, 3}
// 	array2_test := []int{26, 134, 135, 15, 17}
// 	result := SmallestDifference(array1_test, array2_test)
// 	log.Println("Function result:", result)
// }
