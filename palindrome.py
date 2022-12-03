# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:52:18 2020

@author: Bhumi Shah
"""

n = int(input("enter any no"))
rev = 0
new=n
print(n)
while n > 0: 
    a = n % 10
    rev = rev * 10 + a 
    n = n / 10
print(n)
if rev==new:
    print(new," is palindrome")
else:
    print(new," not a palindrome")