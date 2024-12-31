# Conditionals Exerices LEVEL 1

# Getting user input and checking age for driving:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")

# Comparing ages:
my_age = 25  # Replace with your actual age
your_age = int(input("Enter your age: "))

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
else:
    print("We are the same age.")

# Comparing two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# EXERCISE LEVEL 2

# Assigning grades based on scores 
score = int(input("Enter your score: "))

if 80 <= score <= 100:
    print("A")
elif 70 <= score < 80:
    print("B")
elif 60 <= score < 70:
    print("C")
elif 50 <= score < 60:
    print("D")
else:
    print("F")

# Checking Season
month = input("Enter the month: ")

if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month.")

# Modifying fruit list
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter the fruit: ")

if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Modified list: ", fruits)

# EXERCISE LEVEL 3
# Checking skills in the person dicitonary

person = {
    'first_name': 'Muhammed',
    'last_name': 'Kabir',
    'age': 25,
    'country': 'Nigeria',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Daura Road',
        'zipcode': '000186'
    }
}

# Check for middle skill
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print("Middle skill:", middle_skill)

# Check for Python skill
if 'skills' in person and 'Python' in person['skills']:
    print("Python is in the skill set")

# Determine developer type
person = {
    'first_name': 'Muhammed',
    'last_name': 'Kabir',
    'age': 25,
    'country': 'Nigeria',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Daura Road',
        'zipcode': '00186'
    }
}

# 1. Check for middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print("Middle skill:", middle_skill)

# 2. Check for Python skill
if 'skills' in person and 'Python' in person['skills']:
    print("Python is in the skill set")

# 3. Determine developer type
if 'skills' in person:
    skills = person['skills']
    if len(skills) == 2 and 'JavaScript' in skills and 'React' in skills:
        print("He is a front end developer")
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print("He is a backend developer")
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# 4. Print married and living in Nigeria info
if person['is_marred'] and person['country'] == 'Nigeria':
    print(f"{person['first_name']} {person['last_name']} lives in Nigeria. He is married.")



