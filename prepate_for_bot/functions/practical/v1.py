'''
1: Read and Write to a File => Write a function that reads a text file and writes its contents to a new file with each line numbered.
2: Filter List Based on Condition => Create a function that takes a list of numbers and returns a new list containing only numbers that are greater than 10.
3: Parse and Extract Data from a URL => Develop a function that takes a URL string and returns the domain name.
4:  Format Date and Time => Write a function that takes a datetime object and returns a string formatted as "YYYY-MM-DD HH:MM".
5: Generate Random Password: Create a function that generates a random password containing letters, digits, and special characters, with a specified length.
6: Validate an Email Address:  Develop a function that checks if a given string is a valid email address.
7: Calculate Age from Date of Birth: Write a function that calculates a person's age in years from their date of birth.
8: Convert Dictionary to JSON String:  Create a function that takes a dictionary and returns a JSON string.
9: Check Connectivity to a Website: Develop a function that checks if your computer can connect to a specified website.
10: Batch Rename Files: Write a function that renames all files in a specified directory based on a naming pattern and increments.

'''

def filter_condition(list):
    return [num for num in list if num >= 10]
print(filter_condition([1, 5, 6, 3, 56, 10]), "<======================= 2 task.")
  
