# Write a Python program to count occurrences of a substring in a string.
mainsstring=str(input("Enter the main string: "))
substring=str(input("Enter the substring to count: "))
count=0
for i in range(len(mainsstring)-len(substring)+1):
    if mainsstring[i:i+len(substring)]==substring:
        count+=1
print("The substring",substring,"occurs",count,"times in the main string.")