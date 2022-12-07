newstring=''
print("Enter 'q'/'Q' for exit.");
word = input("Enter any string : ");
if word== 'q' or word=='Q':
    exit();
for x in word:
    if x.isupper() == True:
        newstring+=x.lower()
    else:
        newstring+=x.upper()  
print(newstring)
##Enter 'q' for exit.
##Enter any string : asFG
##ASfg


