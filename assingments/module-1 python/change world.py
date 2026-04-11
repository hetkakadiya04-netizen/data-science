# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string 
string = input("Enter a string: ")
not_index = string.find("not")
poor_index = string.find("poor")
if not_index != -1 and poor_index != -1 and not_index < poor_index:
    string = string[:not_index] + "good" + string[poor_index + 4:]
print("The modified string is:", string)