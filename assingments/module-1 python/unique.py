# Write a Python program to get unique values from a list.
list = input("Enter a list of values separated by spaces: ").split()
unique_values = list(set(list))
print("The unique values from the list are:", unique_values)