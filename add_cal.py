# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:44:37 2022

@author: singh
"""

def add_cal(a,b):
    return a+b
def sub_cal(a,b):
    return a-b
def multi_cal(a,b):
    return a*b
def divide_cal(a,b):
    return a/b
def rem_cal(a,b):
    return a%b
print('select the operator')
print('1.Add')
print('2.substract')
print('3.multiple')
print('4.divide')
print('5.remender')
while True:
    choice = input("Enter your choice (1/2/3/4/5) : ")
    if choice in ('1','2','3','4','5'):
        n1=float(input("Enter first number"))
        n2=float(input("Enter second number"))
        if choice == '1':
            print(n1,'+',n2,'=',add_cal(n1,n2))
        elif choice == '2':
            print(n1,'-',n2,'=',sub_cal(n1,n2))
        elif choice == '3':
            print(n1,'*',n2,'=',multi_cal(n1,n2))
        elif choice == '4':
            print(n1,'/',n2,'=',divide_cal(n1,n2))
        elif choice == '5':
            print(n1,'%',n2, '=',rem_cal(n1,n2))
        break
    else:
            print('Please Enter a vailid input')