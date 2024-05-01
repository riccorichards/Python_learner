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

# level 2 N2
def find_max_without_build_in(list):
    max_num = list[0]
    for num in list:
        if(max_num < num):
            max_num = num
    return max_num       
nums = [0, 5, 6, 3, 2, 1, 5, 6, 8, 9, -5, 4]

# level 2 N3
def avg_nums(list):
    return sum(list) / len(list)

# level 2 N4
def capital_case(str):
    return str.title()

# level 2 N5
def sorted_list(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
    
# level 2 N6
def character_occurrences(str):
    hash_table = {}
    for char in str:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1
    return hash_table 

# level 2 N7
def is_prime_num(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n & 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True    
    
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

# level 2 N9
def palindrome_checker(str):
    str = str.replace(" ", "").lower()
    return str == str[::-1]

# level 2 N10 
def remove_dup(list):
    return set(list)


#///////////////////////////////////////////////////////////////////////////
'''
1: Convert List of Strings to Integers:  Write a function that takes a list of strings (all representing numbers) and returns a list of integers.
2: Calculate the Median of a List: Create a function that takes a list of numbers and returns the median value.
3: Remove Special Characters from a String: Develop a function that removes all special characters from a string, leaving only letters and numbers.
4: Find the Second Largest Number in a List: Write a function to find the second largest number in a list of numbers.
5: Count the Number of Each Vowel in a String: Create a function that counts and returns the number of each vowel in a given string.
6: Merge Two Lists into a Dictionary: Develop a function that takes two lists, one with keys and one with values, and merges them into a dictionary.
7: Check if All Elements in a List are Unique: Write a function that checks if all elements in a given list are unique (no duplicates).
8: Find All Substrings of a String: Create a function that returns a list of all substrings of a given string.
9: Format a String of Names: Develop a function that takes a list of dictionaries (each with a 'name' key) and returns a string formatted as a comma-separated list of names, with an "and" before the last name.
10: Convert Bytes to a Human-Readable Format: Write a function that takes the size of a file in bytes and converts it into a human-readable format (e.g., converting 1024 bytes to '1 KB').
'''

def convert_str_into_int(list):
   return [int(num) for num in list]

def mediana(list):
    sort = sorted(list)
    n = len(sort)
    half = int((len(list) - 1) / 2)
    if n % 2 == 0:       
        return (sort[half] + sort[half + 1]) / 2
    else: 
        return sort[half]

def remove_spaces(str):
    return str.replace(" ", "")

def second_largest_num(nums):
    max_num = float('-inf')
    second_num = float("-inf")
    for num in nums:
        if num > max_num:
            second_num = max_num
            max_num = num
        elif max_num > num > second_num:
            second_num = num
    return second_num 

def vowel_counter(str):
    vowels = "aeiou"
    result = {v: 0 for v in vowels}
    for char in str.lower():
        if char in result:
            result[char] += 1
    return result

def merge_lister(key_list, value_list):
    return {k: v for k , v in zip(key_list, value_list)}

def unique_checker(nums):
    stored_values = []
    for item in nums:
        if item in stored_values:
            return False
        else:
            stored_values.append(item)
    return True

def all_substrings(s):
    substrings = []
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            substrings.append(s[start:end])
    return substrings

def names_string(names):
    names_in_string_formatting = ""
    for i in range(len(names)):
        if(i + 1 < len(names)):
            names_in_string_formatting += names[i]["name"] + ", "
        elif i + 1 == len(names):
            names_in_string_formatting += "and " + names[i]["name"]        
    return names_in_string_formatting

def convert_bytes(bytes):
    human_readable = bytes / 1024
    return str(human_readable) + " kb"

'''
1: Calculate the Mode of a List: Write a function that takes a list of numbers and returns the mode (the number that appears most frequently).
2: Case-insensitive String Comparison: Create a function that compares two strings case-insensitively and returns True if they are the same, otherwise False.
3: Extract File Extension: Develop a function that takes a filename string and returns its file extension.
4: Implement a Basic Stack: Write a function that implements a simple stack with push, pop, and peek operations.
5: Group Elements by Parity: Create a function that takes a list of integers and returns two lists, one containing all even integers and the other containing all odd integers.
6: Validate IP Address: Develop a function that checks if a given string is a valid IPv4 address.
7: Calculate Compound Interest: Write a function that calculates compound interest given principal, annual rate of interest, number of times interest applied per time period, and number of time periods.
8: Convert Snake Case to Camel Case: Create a function that takes a snake_case string and converts it to camelCase.
9: Find the Longest Word in a Sentence: Develop a function that finds and returns the longest word in a given sentence.
10: Normalize an Array: Write a function that normalizes an array of integers to a scale of 0 to 1 (where 0 is the smallest value in the array and 1 is the largest).

'''
def list_mode(nums):
    hash_table = {}
    for num in nums:
        hash_table[num] = hash_table.get(num, 0) + 1
    return hash_table
print(list_mode([1, 32, 2, 5, 6, 4, 5, 3, 5, 4, 3, 2, 6, 5, 10, 45]))