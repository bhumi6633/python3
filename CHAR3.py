# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:02:46 2019

@author: Smriti
"""
x=97# ascii number for a 
for r in range(1,5):
    for c in range(1,5):
        print(chr(x),end=' ')
    x=x+1
    print()
    
#1  A A A A
#2  B B B B
#3  C C C C
#4  D D D D
print('****************')

for r in range(1,5):
    x=65
    for c in range(1,5):
        print(chr(x),end=' ')
        x=x+1
    print()
#1 A B C D   
#2 A B C D
#3 A B C D
#4 A B C D
print("*****************")   
x=97
for r in range(1,5):
    for c in range(1,5):
        print(chr(x),end=' ')
        x=x+1
    print()

#1 A B C D
#2 E F G H
    
