// The exercise describes a probability calculation in a simplified version of Blackjack, focusing on the dealer's actions.
// The dealer draws cards until they reach or exceed a specified target value with their hand.
// The goal is to compute the probability that the dealer will exceed (bust) the target given their starting hand.

// Problem Explanation
// The dealer will continue drawing cards until their hand's sum is at least the target minus 4,
// simulating that in a traditional game the dealer stands on 17 and draws on 16.
// Each card drawn has a uniform probability of being any value from 1 to 10.

// Steps to Solve

// Define the Parameters:
// target: The value that the dealer tries not to exceed.
// startingHand: The initial value of the dealer's hand.

// Calculate Probability of Busting:
// If the starting hand is already greater than the target, the probability of busting is 100%.
// If the starting hand plus 10 (maximum possible card value) is still below the target,
// the probability of busting is 0% because the dealer cannot possibly bust in the next draw.

// Recursive Probability Calculation:
// For each possible card value from 1 to 10, compute the new hand value and recursively calculate the probability of busting from that new state.
// The recursive function should consider the probability of drawing each card (which is 0.1 or 1/10), and sum the probabilities weighted by these chances.

// Base Cases:
// If the current hand is already greater than the target, return 1 (100% bust).
// If the current hand plus 10 is less than the target, return 0 (cannot bust on next card).

// Memoization:
// Use a map to store already computed probabilities for certain hand values to optimize the computation and avoid recalculating
// for the same hand value multiple times.

// SOLUTION 1 //
package main

import "math"

func calculateProbability(currentHand int, target int, memo map[int]float64) float64 {
	if value, ok := memo[currentHand]; ok {
		return value
	}
	if currentHand > target {
		return 1
	}
	if currentHand+4 >= target {
		return 0
	}

	totalProbability := 0.0
	for drawnCard := 1; drawnCard <= 10; drawnCard++ {
		totalProbability += 0.1 * calculateProbability(currentHand+drawnCard, target, memo)
	}

	memo[currentHand] = totalProbability
	return totalProbability
}

func BlackjackProbability(target int, startingHand int) float64 {
	memo := make(map[int]float64)
	return math.Round(calculateProbability(startingHand, target, memo)*1000) / 1000
}
