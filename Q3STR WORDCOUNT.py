phrase = input("Enter a sentence:")

# to find the total no. of alphabets and numbers
a=0
for x in phrase:
    if x.isalnum():
        a+=1  

words = phrase.split()# to separate the words in a string
wordcount = len(words)# no. of words
c=len(phrase)# no of characters

print("The total word count is:",wordcount)
print("no of characters",c)
print("total alphanumeric",a)
print("percentage of alphanumeric values",a/c*100,'%')
        

