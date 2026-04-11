# Write a Python program to count the occurrences of each word in a given sentence.
string=str(input("Enter a sentence: "))
word_count={}
for word in string.split():
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1  
print("The occurrences of each word in the sentence are:")
for word, count in word_count.items():
    print(word, ":", count)
