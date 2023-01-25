"""
Author: Amrit Manash
Created On : 25th Jan 2023
"""

#Assigning a range of numbers to list and then printing the list

myList  = [*range(1,11)]
print(myList)

prod = 1

for i in myList:
    prod = prod *i

print("The final product of all numbers in a list is: ",prod)
