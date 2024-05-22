// The exercise requires writing a function that takes an array of distinct integers and a target sum,
// then finds all unique quadruplets within the array that sum up to the given target.
// The solution should return these quadruplets as a two-dimensional array.

// Approach to Solve the Problem:
// This problem can be approached in a way similar to the "two-sum" problem but extended to handle four numbers.
// An efficient approach is to use a combination of hashing and pair-sums:

// Precompute Pair Sums:
// Use a hash map to store pairs of numbers and their sums. For each sum, you store a list of pairs (as tuples or arrays) that add up to that sum.

// Find Quadruplets:
// For each pair in the hash map, check if the complement (target sum minus the current pair sum) exists in the hash map.
// Ensure that the indices of the elements in the two pairs do not overlap to maintain distinct integers in the quadruplets.

// Avoid Duplicates:
// To avoid duplicates, you can sort each potential quadruplet and store them in a set (or check before adding to the result list if the result list is sorted and converted to a set).

package main

//import "log"

func FourNumberSum(array []int, target int) [][]int {
	all_pair_sums := map[int][][]int{}
	quadruplets := [][]int{}
	for index := 1; index < len(array)-1; index++ {
		for j_index := index + 1; j_index < len(array); j_index++ {
			current_sum := array[index] + array[j_index]
			difference := target - current_sum
			if pairs, found := all_pair_sums[difference]; found {
				for _, pair := range pairs {
					newquad := append(pair, array[index], array[j_index])
					quadruplets = append(quadruplets, newquad)
				}
			}
		}
		for k_index := 0; k_index < index; k_index++ {
			current_sum := array[index] + array[k_index]
			all_pair_sums[current_sum] = append(all_pair_sums[current_sum], []int{array[k_index], array[index]})
		}
	}
	return quadruplets
}

// UNBLOCK FOR TEST
// func main() {
// 	array := []int{7, 6, 4, -1, 1, 2}
// 	target := 16
// 	result := FourNumberSum(array, target)
// 	log.Println(result) // Output can be [[7, 6, 4, -1], [7, 6, 1, 2]] depending on input array order
// }
