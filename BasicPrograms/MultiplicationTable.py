"""
Author: Amrit Manash
Created On: 25th Jan 2023
"""
num = int(input("Enter a number for which you want to see the Multiplication table"))
c=num
ct=1
for i in range(1,11):
    print(c," X ",ct," = ",num*i)
    ct+=1
