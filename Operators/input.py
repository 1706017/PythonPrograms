"""
Author : Amrit Manash
Created On : 23rd Jan 2023
"""

name = input("Enter your name")
print("Your name is ",name)

#Here we are doing type casting to int since by default the input type is of string type
num = int(input("Enter a number"))
print("The number is ",num)

#To take multiple input from user by some separator or delimiter
myNumList = [int(x) for x in input("Enter three numbers separted by space").split()]
print(myNumList)

myNewList = [int(x) for x in input("Enter three numbers separated by comma").split(',')]
print(myNewList)

