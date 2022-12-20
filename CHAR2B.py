# -*- coding: utf-8 -*-
"""
@author: Bhumi
"""

x=65#ascii value of A
for i in range(1,5):
    for j in range(1,5):
        print(chr(x),end=' ')
        x=x+1
    print()