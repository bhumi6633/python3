x=''
s=0
z=input("Enter string:")
for a in z:
    if a.isdigit():
        x+=a# x=x+a shifting the digits in x
for i in x:
    s+=int(i)
    
print("string ",z)
print("digits ",x)
print("addition of digits",s)


#x=x+a == x+=a
#x=x-a == x-=a
#x=x*a == x*=a 