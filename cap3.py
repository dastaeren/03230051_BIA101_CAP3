
# Github Repo link: https://github.com/dastaeren/03230051_BIA101_CAP3 
# Your Name: Deki Yangzom
# Your Section: A
# Your Student ID Number: 03230051

# REFERENCES
#  https://youtu.be/BRrem1k3904?si=qY50UkN7maRS-QDI
# https://www.youtube.com/watch?v=bnSYeYFRCaA 
# https://www.w3schools.com/python/ref_string_isnumeric.asp 
# https://www.geeksforgeeks.org/file-handling-python/

# SOLUTION
# The total sum of from the given input file 051.txt is 487782

def load_input(file_path): #Reads the input file and returns a list of lines.

    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def extract_numbers(line): #Extracts the first and last digit in a line and returns a two-digit number.
    try:
        first_num = next(char for char in line if char.isnumeric())
        last_num = next(char for char in reversed(line) if char.isnumeric())
        return int(first_num + last_num)
    except StopIteration:
        return 0

def analyze_file(file_path): #Processes the input file, calculates the two-digit numbers for each line, and returns the total sum.
    total_sum = 0
    lines = load_input(file_path)
    for line in lines:
        line = line.strip()
        if line:  # Ensure the line is not empty
            num = extract_numbers(line)
            print(f"Extracted number from line '{line}': {num}")  #Show extracted number
            total_sum += num
    return total_sum

def display_results(file_path): #Prints the total sum from the given input file, showing the process line by line.

    total_sum = analyze_file(file_path)
    print(f"\nThe total sum from the given input file {file_path} is {total_sum}\n")

# Specify the path to the input file
file_path = '051.txt'

# Call the display_results function to output the results
display_results(file_path)


