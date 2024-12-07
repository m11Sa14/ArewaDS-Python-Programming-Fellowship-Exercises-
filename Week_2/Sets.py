# Sets Exercises: Level 1

# Finding the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length_of_it_companies = len(it_companies)

# Adding 'Twitter' to it_companies
it_companies.add('Twitter')

# Inserting multiple IT companies at once to the set it_companies
it_companies.update({'LinkedIn', 'Snapchat', 'WhatsApp'})

# Removing one of the companies from the set it_companies
it_companies.remove('Apple')  # or use discard method

# What is the difference between remove and discard
# remove will raise a KeyError if the item to remove is not found in the set.
# discard will not raise an error if the item is not found in the set.

# Sets Exercises: Level 2

# Joining A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A_B_union = A.union(B)

# To Find A intersection B
A_B_intersection = A.intersection(B)

# Is A subset of B
is_subset = A.issubset(B)

# Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)

# To Join A with B and B with A
A_B_union = A.union(B)
B_A_union = B.union(A)

# What is the symmetric difference between A and B
A_B_symmetric_difference = A.symmetric_difference(B)

# Deleting the sets completely
del A
del B

# Sets Exercises: Level 3

# Converting the ages to a set and compare the length of the list and the set, which one is bigger?
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_set = set(ages)
list_length = len(ages)
set_length = len(ages_set)
bigger = 'list' if list_length > set_length else 'set'


# Explaining the difference between the following data types: string, list, tuple, and set

# String: A sequence of characters enclosed in quotes. Immutable.
# List: An ordered collection of items which can be of different types. Mutable and allows duplicates.
# Tuple: Similar to lists, but immutable. Ordered collection of items.
# Set: An unordered collection of unique items. Mutable but does not allow duplicates.

# To count How many unique words have been used in the sentence?
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
number_of_unique_words = len(unique_words)










