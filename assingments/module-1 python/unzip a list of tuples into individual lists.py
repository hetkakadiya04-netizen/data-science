# Write a Python program to unzip a list of tuples into individual lists.
list_of_tuples = input("Enter a list of tuples (e.g., (1, 'a'), (2, 'b')): ")
list_of_tuples = eval(list_of_tuples)
unzipped_lists = list(zip(*list_of_tuples))
for i, unzipped in enumerate(unzipped_lists):
    print(f"List {i + 1}: {list(unzipped)}")