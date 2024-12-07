# Declaring an empty list
empty_list = []

# Declaring a list with more than five items
my_list = [1, 2, 3, 4, 5, 6, 7]

# Finding the length of my list
length_of_list = len(my_list)

# Getting the first, middle and the last item of my list
first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[-1]

# Declaring a list called mixed_data_types
mixed_data_types = ['Your Name', 25, 1.75, 'Single', '123 Your Address St.']

# Declaring a list variable named it_companies and assign initial values
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Printing the list using print()
print(it_companies)

# printing the number of companies in the list 
number_of_companies = len(it_companies)
print(number_of_companies)

# printing First,middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# Printing the list after modifying one of the companies 
it_companies[0] = 'Meta'
print(it_companies)

# Adding an IT company to it_companies
it_companies.append('Tesla')
print(it_companies)

# Inserting IT company in the middle of the company list
it_companies.insert(len(it_companies) // 2, 'Zoom')
print(it_companies)

# Changing one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Joining the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# Checking if a certain company exists in the it_companies list
exists = 'Facebook' in it_companies
print(exists)

# Sorting the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# Slicing out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# Slicing out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index-1:middle_index+1]
else:
    middle_companies = it_companies[middle_index]
print(middle_companies)

# Removing the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Removing the middle IT company or companies from the list
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# Removing the last IT company from the list
it_companies.pop()
print(it_companies)

# Removing all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroying the IT companies list
del it_companies

# Joining the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

# Copying the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux
full_stack = joined_list.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)

# EXERCISE LEVEL 2

# Sorting the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age, "Max age:", max_age)


# Adding the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# Finding the median age
middle_index = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]
print("Median age:", median_age)

# Finding the average age
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

# Finding the range of the ages
age_range = max_age - min_age
print("Range of ages:", age_range)

# Comparing the value of (min - average) and (max - average) using abs()
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Min difference:", min_diff, "Max difference:", max_diff)


# Finding the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = [countries[middle_index]]
print("Middle country(ies):", middle_countries)

# Dividing the countries list into two equal lists
first_half = countries[:middle_index + (len(countries) % 2)]
second_half = countries[middle_index + (len(countries) % 2):]
print("First half:", first_half, "Second half:", second_half)

# Unpacking the first three countries and the rest as scandic countries
# first, second, third, *scandic_countries = countries
print("First three countries:", first, second, third)
print("Scandic countries:", scandic_countries)




















