# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:16:52 2019

@author: Bhumi
"""
#REVERSE 
s=0
n=int(input("enter any number"))
while n!=0:
    r=n%10
    s=r+s*10
    n=n//10
print(s)
print(n)
#n     r=n%10      s=r+s*10    n=n//10
#345   5=345%10    5=5+0*10    34=345//10
#34    4=34%10     54=4+5*10    3=34//10
#3     3=3%10      543=3+54*10  0 =3//10
    