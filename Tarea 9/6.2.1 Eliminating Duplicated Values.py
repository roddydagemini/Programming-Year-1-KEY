# Ask the user to input the number list WITH commas to separate the numbers
number = input("Please create a list of numbers that will elimate duplication of values: ")
# Within the list we aim to make the numbers into a list of integers instead of one big string
number_list = number.split()
# this is what creates the  list of the unique numbers
unique_numbers = []
# Loop through each item within the list
for num in number_list:
    num = int(num)
    # Checks if the number is not already in the list of unique numbers
    if num not in unique_numbers:
        unique_numbers.append(num)
        # Tells the program to space out the numbers using a space 
print("List without duplicates:", * unique_numbers)