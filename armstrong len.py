# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:23:33 2020

@author: USER
"""


x=int(input("enter any number"))
t=x 
t2=x
len1=0
sum1 = 0
# to check length of digit [len(x)]
while(t2!=0):
    len1=len1+1 #len1+=1    
    t2=t2//10
print("length of x is=",len1)
# to find the sum of digit to the pow of its length
while (t!=0): 
    r = t%10
    sum1 = sum1 + pow(r,len1) 
    t = t//10
#print(sum1)
if sum1==x:
    print("armstrong")
else:
    print("not armstrong")