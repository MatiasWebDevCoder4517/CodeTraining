# Write a Python function that will create and return a dictionary from another dictionary, but sorted by value.
# You can assume the values are all comparable and have a natural sort order.

# Ex:
# composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

# Expected output:
# sorted_composers = {'Wolfgang': 35, 'Frederic': 39, 'Ludwig': 56, 'Johann': 65}

# Hints:

# Remember if you are using Jupyter notebook to use `print()` to view your dictionary in it's natural ordering (in case Jupyter displays your dictionary sorted by key).
# Also try to keep your code Pythonic - i.e. don't start with an empty dictionary and build it up one key at a time - look for a different, more Pythonic, way of doing it.

# --> You'll likely want to use Python's `sorted` function.


## PSEUDOCODE

# Sub-objetives:
# 1. create a new dict from a original dict
# 2. sort the values of the keys from lower to upper

# code strategy:
# 1) create a shallow copy of the original dict
# 2) iterate the values of the copied dict
# 3) determine within 2 values which is greater. Repeat this until the last one
# 4) build the dict at the same time executing point 3.

# testing:

# 1) values of the keys must be integers only. Otherwise modify to 0 (as number).


## SOLUTION 1:
def get_sorted_dict(dict_to_sort: dict[str, int]) -> dict[str, int]:
    dict_to_sort = {key: value
        for key, value in sorted(dict_to_sort.items(), key=lambda element: element[1])}
    return dict_to_sort


## SOLUTION 2:
def sort_dict_by_values(input_dict):
    # Create a list of tuples from the dictionary items
    items = list(input_dict.items())

    # Implement an insertion sort on the list of tuples based on the second element (the value)
    for i in range(1, len(items)):
        key_item = items[i]
        j = i - 1

        # Move elements of items[0..i-1], that are greater than key_item, to one position ahead
        # of their current position
        while j >= 0 and items[j][1] > key_item[1]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key_item

    # Convert the sorted list of tuples back into a dictionary
    sorted_dict = {k: v for k, v in items}
    return sorted_dict


# Example usage
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
sorted_composers = sort_dict_by_values(composers)
print(sorted_composers)

## testing
dict_test_unsorted = {"Johann": 65, "Ludwig": 56, "Frederic": 39, "Wolfgang": 35}
print(get_sorted_dict(dict_test_unsorted))
