# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:39:06 2020

@author: Bhumi Shah
"""

#5!- 1*2*3*4*5
#p=1
#for i in range(1,6):
#    p=p*i
#print(p)

#i*p=p
#1*1=1
#2*1=2
#3*2=6
#4*6=24
#5*24=120

#n!- 1*2*3*4*....n!

#n=int(input("enter n"))
#p=1
#for i in range(1,n):
#    p=p*i
#print(p)
 
##1!, 2!,  3! , 4!

#n=int(input("enter n"))
#p=1
#for i in range(1,6):
#    p=p*i
#    print(p,end=' ')  

##11.(1*1) + (1*2) + (1*2*3) +(1*2*3*4)
##1!+2!+3!+4!.....
#n=int(input("enter n"))
#p=1
#s=0
#for i in range(1,5):
#    p=p*i
#    s=s+p
#print(s,end=' ') 

#1/1!+1/2!+1/3!.....n
#n=int(input("enter n"))
#f=1
#s=0
#for i in range(1,n):
#    f=f*i
#    s=s+1/f
#print(s,end=' ')

#i     f=f*i       s=s+1/f
#1     1=1*1       1/1=0+1/1
#2     2=1*2          =1/1+1/2

#x/1!+x/2!+x/3!.....
#n=int(input("enter n"))
#f=1
#s=0
#x=int(input("enter x"))
#for i in range(1,n):
#    f=f*i
#    s=s+x/f
#print(s,end=' ')

#i     f=f*i       s=s+x/f
#1     1=1*1       1/1=0+2/1
#2     2=1*2           =1/1+2/2

#(0+1=1) + (1+2=3) + (1+2+3=6) +......n
#1+(1+2)+(1+2+3)+.....

n=int(input("enter n"))
s=0
s1=0
for i in range(1,n):
    s=s+i#inner sum
    s1=s1+s#outer sum
print(s1,end=' ') 

#i   s=s+i      s1=s1+s
#1   1=0+1       1=0+1
#2   3=1+2       4=1+3
#3   6=3+3      10=4+6