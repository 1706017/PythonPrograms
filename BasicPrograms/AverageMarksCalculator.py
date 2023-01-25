"""
Author : Amrit Manash
Created On : 24th Jan 2023
"""

myMarksList =[float(x) for x in input("Enter three subject Marks by Student seprated by space :").split()]
print("The Marks obtained by student are : ", myMarksList)

sum = 0

for x in myMarksList:
    sum=sum+x

average_Marks = sum/3
print("Average Marks Obtained is : ",average_Marks)


