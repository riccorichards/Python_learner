'''
1: Sum of List: Write a function that takes a list of numbers and returns the sum of all numbers in the list.
2: Find Maximum Without max(): Create a function to find the largest number in a list without using the max() function.
3: Calculate Average: Develop a function that calculates the average of numbers in a list.
4: String to Title Case: Write a function that converts a given string to title case (each word starts with a capital letter).
5: Sort List Without sorted(): Create a function that sorts a list of numbers in ascending order without using the sorted() function.
6: Count Character Occurrences: Write a function that counts how many times a specific character appears in a string.
7: Is Prime Number: Develop a function that takes a number and returns True if the number is a prime number, otherwise False.
8: Generate Fibonacci Sequence: Write a function that returns a list containing the Fibonacci sequence up to n numbers.
9: Palindrome Checker: Create a function that checks if a given string is a palindrome (reads the same forward and backward).
10: Remove Duplicates from List: Develop a function that removes all duplicate values from a list and returns a list of only unique elements.

'''

# level 2 N1
def sum_all_nums(list):
    return sum(list)
print(sum_all_nums([1, 2, 3, 4]), "<============= task 1.")

# level 2 N2
def find_max_without_build_in(list):
    max_num = list[0]
    for num in list:
        if(max_num < num):
            max_num = num
    return max_num       
nums = [0, 5, 6, 3, 2, 1, 5, 6, 8, 9, -5, 4]
print(find_max_without_build_in(nums), "<============= task 2.") 

# level 2 N3
def avg_nums(list):
    return sum(list) / len(list)
print(avg_nums(nums), "<============= task 3.") 

# level 2 N4
def capital_case(str):
    return str.capitalize()
print(capital_case("example"), "<============= task 4.") 

# level 2 N5
def sorted_list(list):
    i = 0
    while i < len(list):
        if(list[i] > list[i+1]):
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
        i += 1
    return list
print(sorted(nums), "<============= task 5.")

# level 2 N6
def character_occurrences(str):
    hash_table = {}
    for char in str:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1
    return hash_table 
print(character_occurrences("hello world"), "<============= task 6.")

# level 2 N7
def is_prime_num(n):
    if(n == 1):
        return False
    elif n > 1:
        for num in range(2, n):
            if(n % num == 0):
                return False
            else:
                return True
print(is_prime_num(16))   

# level 2 N8
def fibonacii_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibonacii_container = [0,1]
        for i in range(2, n):
            next_value = fibonacii_container[-1] + fibonacii_container[-2]
            fibonacii_container.append(next_value) 
    return fibonacii_container
print(fibonacii_sequence(5))

# level 2 N9
def palindrome_checker(str):
    str = str.replace(" ", "").lower()
    return str == str[::-1]
print(palindrome_checker("A man a plan a canal Panama")) 

# level 2 N10 
def remove_dup(list):
    return set(list)
print(remove_dup([1, 2, 1, 3, 5, 6, 4, 1, 2, 3]))