'''
Level 1: Easy Tasks
1: Print Function: Write a function that takes a string as an argument and prints it.
2: Sum of Two Numbers: Create a function that accepts two numbers as arguments and returns their sum.
3: Convert Celsius to Fahrenheit: Write a function that converts Celsius to Fahrenheit using the formula 𝐹=𝐶 × 1.8 + 32.
4: Check Even Number: Develop a function that takes a number and returns True if the number is even, otherwise False.
5: Concatenate Strings: Write a function that takes two strings and returns them concatenated.
6: Find Length of String: Create a function that returns the length of a given string.
7: Multiply Three Numbers: Write a function that takes three numbers as arguments and returns their product.
8: Reverse String: Develop a function that takes a string and returns it reversed.
9: Calculate Area of a Rectangle: Write a function that calculates the area of a rectangle given its width and height.
10: Check Membership: Create a function that takes a list and an item, and returns True if the item is in the list, otherwise False.

'''

# level 1 N1
def define_str(str):
   print(str) 
define_str("hello world!")

# level 1 N2
def num_sum(a,b):
   return a+b
print(num_sum(5,15))

# level 1 N3
def convert_cel_into_fah(x):
   return x * 1.8 + 32
print(convert_cel_into_fah(45))

# level 1 N4
def is_even(n):
   if n % 2 == 0: 
    return True 
   else: return False
print(is_even(4))   

# level 1 N5
def concat_strings(str1, str2):
   return str1 + " " + str2 
print(concat_strings("hello","world"))

# level 1 N6
def define_length_of_string(str):
   return len(str)
print(define_length_of_string("hello"))

# level 1 N7
def multiply(x,y,z):
   return x * y * z
print(multiply(5, 5, 5))

# level 1 N8
def reverse_str(str):
   return str[::-1] # explain please i found this solution in the internet
print(reverse_str("hello world"))

# level 1 N9
def calculate_area_of_rectanguler(width, heigth):
   return (width * heigth)
print(calculate_area_of_rectanguler(15, 5))

# level 1 N10
def check_membership(list, item):
   for el in list:
      if el == item:
         return True
   return False

membership = ["ricco", "ricchards","richo"]
correct_item = "ricchards"
wrong_item = "zaza"
print(check_membership(membership, correct_item))
print(check_membership(membership, wrong_item))