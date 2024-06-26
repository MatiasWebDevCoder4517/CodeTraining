# You have text data spread across multiple servers.
# Each server is able to analyze this data and return a dictionary that contains words and their frequency.

# Your job is to combine this data to create a single dictionary that contains all the words and their combined frequencies from all these data sources.

# Bonus points if you can make your dictionary sorted by frequency (highest to lowest).

# For example, you may have three servers that each return these dictionaries:

# Ex:

# d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
# d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
# d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

# Expected output:

# d = {'python': 17,
#      'javascript': 15,
#      'java': 13,
#      'c#': 12,
#      'c++': 10,
#      'go': 9,
#      'erlang': 5,
#      'haskell': 2,
#      'pascal': 1}

# Hint:
# If only servers 1 and 2 return data (so d1 and d2), your results would look like:

# d = {'python': 16,
#      'javascript': 15,
#      'java': 13,
#      'c#': 12,
#      'c++': 10,
#      'go': 9}

## PSEUDOCODE:

# Sub-objetives:
# 1) count the total value of each unique key between dicts (frequencies)
# 2) sort the result from highest to lowest

# Code-strategy:
# 0) capture *args as dicts, otherwise ignore it -> CHECK
# 1) shallow copy of the largest dict
# 2) iterate the rest of dicts and refill the shallow copy dict with the keys that don't exist, the additional values must be added


## SOLUTION 1:
def get_data_frequency(*dicts: dict[str, int]) -> dict[str, int]:
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v

    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))


d1 = {"python": 10, "java": 3, "c#": 8, "javascript": 15}
d2 = {"java": 10, "c++": 10, "c#": 4, "go": 9, "python": 6}
d3 = {"erlang": 5, "haskell": 2, "python": 1, "pascal": 1}
print(get_data_frequency(d1, d2, d3))
