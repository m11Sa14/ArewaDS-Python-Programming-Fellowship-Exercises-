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

# Exercise MODULE 3 
age = 28 # declaring age as an interger variable 
height = 7.5 # declaring height as a float variable
complex_number = # declaring a variable that stores a complex number 

# Script to calculate area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("Area of the triangle is", area)

# Script to calculate perimeter of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

# Script to calculate area and perimeter of a rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is", area)
print("The perimeter of the rectangle is", perimeter)

# Script to calculate area and circumference of a circle
import math

radius = float(input("Enter the radius: "))
pi = 3.14
area = pi * (radius ** 2)
circumference = 2 * pi * radius
print("The area of the circle is", area)
print("The circumference of the circle is", circumference)

# Equation: y = 2x - 2
slope = 2
x_intercept = 2 / 2  # Setting y = 0 to find x
y_intercept = -2  # Setting x = 0 to find y
print("Slope:", slope)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

# Slope and distance between points (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Slope:", slope)
print("Euclidean Distance:", euclidean_distance)

slope_task_8 = 2
slope_task_9 = (10 - 2) / (6 - 2)
comparison = slope_task_8 == slope_task_9
print("Are the slopes equal?", comparison)

# Script to calculate value of y
x = -3  # Example value where y is 0
y = x**2 + 6*x + 9
print("For x =", x, ", y =", y)

# Falsy comparison
length_python = len('python')
length_dragon = len('dragon')
falsy_comparison = length_python != length_dragon
print("Falsy comparison statement:", falsy_comparison)
check = 'on' in 'python' and 'on' in 'dragon'
print("Is 'on' in both 'python' and 'dragon'?", check)

# checking if jargon is a sentence
sentence = "I hope this course is not full of jargon."
check_jargon = 'jargon' in sentence
print("Is 'jargon' in the sentence?", check_jargon)

# Checking if 'on' is Not in Both 'python' and 'dragon
check_not_in = 'on' not in 'python' and 'on' not in 'dragon'
print("There is no 'on' in both 'dragon' and 'python':", check_not_in)

# Converting Length of 'python' to Float and then to String
length_python = float(len('python'))
length_python_str = str(length_python)
print("Length of 'python' as float and then string:", length_python_str)

# Checking if a Number is Even
number = 4  # Example number
is_even = number % 2 == 0
print("Is the number even?", is_even)

# Checking if Floor Division of 7 by 3 Equals 2.7
floor_division_check = 7 // 3 == int(2.7)
print("Is the floor division of 7 by 3 equal to int(2.7)?", floor_division_check)

# Checking if Type of '10' is Equal to Type of 10
type_check = type('10') == type(10)
print("Is type of '10' equal to type of 10?", type_check)

# Checking if int('9.8') Equals 10
try:
    check_int = int(float('9.8')) == 10  # Corrected to handle float conversion first
except ValueError:
    check_int = False
print("Is int('9.8') equal to 10?", check_int)

# Calculating Pay Based on Hours and Rate
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is", pay)

# Calculating Number of Seconds in a Given Number of Years
years = float(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

# Displaying a table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

# EXERCISE MODULE 4 

# Concatenate strings
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
result = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
print(result)  

# Concatenate more strings
str5 = 'Coding'
str6 = 'For'
str7 = 'All'
result2 = str5 + ' ' + str6 + ' ' + str7
print(result2)  

# Declare and assign variable
company = "Coding For All"

# Print the variable
print(company) 

# Print the length of the company string
print(len(company))  

# Change to uppercase
print(company.upper())  

# Change to lowercase
print(company.lower())  

# Use capitalize(), title(), swapcase() methods
print(company.capitalize()) 
print(company.title())       
print(company.swapcase())    

# Slicing out the first word
first_word = company.split()[0]
print(first_word)  

# Checking if contains 'Coding'
print(company.index('Coding'))  
print(company.find('Coding'))  

# Replacing 'Coding' with 'Python'
new_company = company.replace('Coding', 'Python')
print(new_company)  

# Replacing 'Python for Everyone' with 'Python for All'
phrase = "Python for Everyone"
new_phrase = phrase.replace('Everyone', 'All')
print(new_phrase) 
# Spliting using space as the separator
print(company.split()) 

# Spliting at the comma
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', '))  

# Character at index 0
print(company[0])  

# Last index of the string
print(company[-1]) 

# Character at index 10
print(company[10])  

# Creating an acronym
def create_acronym(phrase):
    words = phrase.split()
    acronym = ''.join([word[0].upper() for word in words])
    return acronym

print(create_acronym('Python For Everyone'))  

# Acronym for 'Coding For All'
print(create_acronym('Coding For All'))  

# First occurrence of 'C'
print(company.index('C'))  

# First occurrence of 'F'
print(company.index('F'))  

# Last occurrence of 'l'
company = "Coding For All People"
print(company.rfind('l'))  

# First occurrence of 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))  

# Last occurrence of 'because'
print(sentence.rindex('because'))  

# Slicing out 'because because because'
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
sliced_phrase = sentence[start:end]
print(sliced_phrase)  

# Does 'Coding For All' Start with 'Coding'?
print(company.startswith('Coding'))  

# Does 'Coding For All' End with 'coding'?
print(company.endswith('coding'))  

# Removing trailing spaces
trimmed_company = '   Coding For All      '.strip()
print(trimmed_company)  

# Checking isidentifier()
print('30DaysOfPython'.isidentifier())  # Output: False
print('thirty_days_of_python'.isidentifier())  

# Joining  list with hash and space
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)  

# using the New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# using the Tab escape sequence
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# String formatting for circle area
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# string formatting of Arithmetic operations
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

























