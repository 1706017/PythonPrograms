"""
Author: Amrit Manash
Created On : 25th Jan 2023
"""
x = int(input("Enter the lower limit"))
y = int(input("Enter the upper limit"))

c=x

while c>=x and c<=y:
    if c%2 != 0:
        print(c)
    c+=1
