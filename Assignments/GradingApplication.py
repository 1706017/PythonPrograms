"""
Author : Amrit Manash
Created On : 24th Jan 2023
"""

students_marks = [float(x) for x in input("Enter your Three Subject marks seprated by space").split()]

c= 0

for marks in students_marks:
    if marks <35:
        c=c+1

if c!=0:
    print("Sorry You have failed in your Exam")
else:
    sum=0
    for i in students_marks:
        sum=sum+i
    avg_marks = sum/3
    if avg_marks<=59:
        print("Your Grade is C")
    elif avg_marks<=69:
        print("Your Grade is B")
    else:
        print("Congratulations Your Grade is A and YOU excell the exam !!!")