#  Write a Python program to find the second smallest number in a list.
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
unique_numbers = list(set(numbers))
if len(unique_numbers) < 2:
    print("There is no second smallest number.")
else:
    unique_numbers.sort()
    print("The second smallest number is:", unique_numbers[1])