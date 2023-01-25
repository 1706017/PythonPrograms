"""
Author: Amrit Manash
Created On: 25th Jan 2023
"""
myList = [int(x) for x in input("Enter the numbers sperated by space").split()]
print(myList)

my_newList = []

for each_value in myList:
    if each_value not in my_newList:
        my_newList.append(each_value)
print("My New Unique List without duplicates: ",my_newList)
print("My Old List with duplicated values: ",myList)

