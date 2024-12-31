# Creating an Empty ditionary called dog
dog = {}

# Adding name, color, breed, legs, age to the dog dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'Nigeria',
    'city': 'Abuja',
    'address': {
        'street': '123 Main St',
        'zipcode': '90001'
    }
}

# Getting the length of the student dictionary:
student_length = len(student)
print(student_length)

# Getting the value of skills and check the data type (should be a list):
skills = student['skills']
print(skills)
print(type(skills))  # This should output <class 'list'>

# Modifying the skills values by adding one or two skills
student['skills'].append('Machine Learning')
student['skills'].append('Deep Learning')
print(student['skills'])

#Getting the dictionary keys as a list:
keys = list(student.keys())
print(keys)

# Getting the dictionary values as a list:
values = list(student.values())
print(values)

# Changing the dictionary to a list of tuples using items() method:
items = list(student.items())
print(items)

# Deleting one of the items in the dictionary:
del student['marital_status']
print(student)

# Deleting one of the dictionaries (let's delete dog):
del dog



