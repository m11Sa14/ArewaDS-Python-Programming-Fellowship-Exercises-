# Tuple Exercises: Level 1

# Creating an empty tuple 
empty_tuple = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Alice", "Jane", "Mary")
brothers = ("John", "Paul", "Mark")

# Joining brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# How many siblings do you have?
number_of_siblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Father", "Mother")
family_members = siblings + parents

# Tuple Exercises: Level 2

# Unpacking siblings and parents from family_members
*siblings, father, mother = family_members

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ("Apple", "Banana", "Mango")
vegetables = ("Carrot", "Potato", "Tomato")
animal_products = ("Milk", "Egg", "Cheese")
food_stuff_tp = fruits + vegetables + animal_products

# Changing the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slicing out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = [food_stuff_lt[middle_index]]

# Slicing out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Deleting the food_stuff_tp tuple completely
del food_stuff_tp

# Checking if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries

# Checking if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries













