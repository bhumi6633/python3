# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:02:46 2019

@author: Smriti
"""

# n=int(input("ente"))
for r in range(1,5):
    for k in range(1,5-r):
        print(end=' ')
    for c in range(1,r+1):
        print('+',end=' ')
    print()        
for r in range(4,1,-1):
    for k in range(1,(5-r)+1):#1,2,3 space
        print(end=' ')
    for c in range(1,r):
        print('+',end=' ')
    print()    