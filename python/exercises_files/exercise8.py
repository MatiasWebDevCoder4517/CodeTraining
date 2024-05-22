#### look at the exercise8.png image in folder exercises_images



## Solution 1:
def has_single_cycle(array):
    num_elements_visited = 0
    current_index = 0
    
    while num_elements_visited < len(array):
        # If we are back at the start before visiting all elements, it's not a single cycle
        if num_elements_visited > 0 and current_index == 0:
            return False
        num_elements_visited += 1
        current_index = get_next_index(current_index, array)
    
    # Check if we're back at the starting index after exactly len(array) moves
    return current_index == 0

def get_next_index(current_index, array):
    jump = array[current_index]
    next_index = (current_index + jump) % len(array)
    return next_index if next_index >= 0 else next_index + len(array)

# Example usage
array = [2, 3, 1, -4, -4, 2]
print(has_single_cycle(array))  # Output: True