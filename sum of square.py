# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:31:26 2020

@author: USER
"""

# 1^2+2^2+3^2.........n

s=0
n=int(input("enter n"))
for x in range(1,n):
    s=s+x**2   
print(s)
    

#x+s=s
#1+0=1
#2+1=3
#3+3=6
#4+6=10
#5+10=15

