# Given two dictionaries, `d1` and `d2`, write a function that creates a dictionary that contains only the keys common to both dictionaries, 
# with values being a tuple containg the values from `d1` and `d2`. 
# (Order of keys is not important).


# Ex:

# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

# Expected output:
# d = {'b': (2, 20), 'c': (3, 30)}

# Hint: Remember that `s1 & s2` will return the intersection of two sets.

# Again, try to keep your code Pythonic - don't just start with an empty dictionary and build it up one by one - think of a cleaner approach.


## PSEUDOCODE:

# Sub-objetives:
# 1) Build a new dict from original dicts
# 2) New dict must have the repeated keys with their respective values as tuples

# code strategy:

# 1) merge both original dicts, save it in a new variable dict
# 2) iterate the new dict removing not repeated keys with their values
# 3) Be sure to add the values as tuples of their keys

## SOLUTION 1:
def common_dict_keys(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys
    d = {k: (d1[k], d2[k]) for k in keys}
    return d


test1_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
test2_dict = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
print(common_dict_keys(test1_dict, test2_dict))