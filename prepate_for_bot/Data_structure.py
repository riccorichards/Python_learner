'''
Define a function named add_two_numbers.

This function should take two parameters, a and b.

The function should return the sum of these parameters.

'''
def add_two_numbers(a, b):
   return a + b 

print(add_two_numbers(15, 50))

# ///////////////////////////////////////////////////////////////////////////////

'''
Task 1: Using len()
Objective: Write a function that takes a list as an argument and returns the number of elements in that list using the len() function.

'''
def define_length(list):
   return len(list)

example_list = [1, 2, 5, 565, "fdsfdfsd", True]
print(define_length(example_list))

'''
Task 2: Using abs()
Objective: Create a function that takes a number and returns its absolute value using the abs() function.

'''
def define_absolute_value(n):
   return abs(n)

print(define_absolute_value(-15))
'''
Task 3: Using sum()
Objective: Write a function that takes a list of numbers as an argument and returns the sum of those numbers using the sum() function.

'''
def define_sum(list):
   return sum(list)


print(define_sum([5, 64 ]))
'''
Task 4: Using round()
Objective: Create a function that takes a floating-point number and returns it rounded to 2 decimal places using the round() function.

'''

def floating_point_num(n):
   return round(n)

print(floating_point_num(25.56))

'''
Task 5: Using max()
Objective: Write a function that takes a list of numbers and returns the largest number using the max() function.

'''

def largest_num(list):
   return max(list)

print(largest_num([2, 5, 65, 23, 2, 0, 23, 56]))

'''
Task 6: Using min()
Objective: Create a function that takes a list of numbers and returns the smallest number using the min() function.

'''

def smallest_num(n):
   return min(n)

print(smallest_num([2, 5, 65, 23, 2, 0, 23, 56]))


'''
Task 7: Using sorted()
Objective: Write a function that takes a list of numbers and returns a new list of these numbers sorted from smallest to largest using the sorted() function.

'''

def sorted_nums(list):
   return sorted(list)

print(sorted([2, 5, 65, 23, 2, 0, 23, 56]))

'''
Task 8: Using type()
Objective: Create a function that takes any Python object and returns the type of that object using the type() function.

'''

def define_type(obj):
   return type(obj)

print(define_type({"name":"ricco"}))

'''
Task 9: Using str()
Objective: Write a function that takes an integer and returns the string version of that integer using the str() function.

'''

def convert_int_into_str(n):
   return str(n)

print(type(convert_int_into_str(45)))

'''
Objective: Create a function that takes a string representing a number and returns the integer version of that number using the int() function.

'''

def convert_str_into_int(str):
   return int(str)

print(type(convert_str_into_int("45")))