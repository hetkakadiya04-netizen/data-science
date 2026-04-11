# Write a Python program to check whether a list contains a sublist. 
list = input("Enter the main list (comma separated): ").split(",")
sublist = input("Enter the sublist (comma separated): ").split(",")
def is_sublist(main_list, sub_list):
    return all(item in main_list for item in sub_list)
if is_sublist(list, sublist):
    print("The main list contains the sublist.")
else:
    print("The main list does not contain the sublist.")
    
    