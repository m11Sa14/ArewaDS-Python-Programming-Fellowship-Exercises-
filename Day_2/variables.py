#Day 2 of 30 of Python programmming 
first_name = "MUHAMMED"
last_name = "KABIR"
full_name = first_name + " " + last_name 
country = "NIGERIA"
city = "KADUNA"
age = "25"
year = 2024
is_married = False
is_true = True
is_light_on = True 


# Declaring multiple variables in one line 
first_name, last_name, country, age, is_married = "MUHAMMED", "KABIR", "NIGERIA", "25", "False"
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('County:', country)
print('Age:', age)
print('Is married:', is_married)


# Checking the Data Types using the type() built in functions
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Finding the length of first_name 
print(len(first_name))
# Comparing the length of first_name and last_name
print(len(first_name) > len(last_name))

# Performing Arithmetic Operations 
num_one = 5
num_two = 4 
total = num_one + num_two
diff = num_two - num_one 
product = num_two * num_one
division = num_one / num_two
remainder = num_one / num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

#Circle calculations
radius = 30
area_of_circle = 3.14159 * radius ** 2
circum_of_circle = 2 * 3.14159 * radius 
print(area_of_circle, circum_of_circle)
# Taking the radius as user input to calculate the area 
radius = float(input("Enter the radius of a circle: "))
print(area_of_circle)

# Using the built in functions to get the first name and others and storing them
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age")
print(first_name, last_name, country, age)

# To check for python reserved words or keywords
help('keywords')





