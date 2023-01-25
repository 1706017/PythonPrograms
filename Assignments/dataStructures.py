"""
Author: Amrit Manash
Created On : 21st Jan 2023

"""

marks = {"Amrit":['BigData','Python','Pyspark','Hive'],
         "Manash":['Java','Spring'],
         "Kalim":['Python','Django']}

#it will return a list of keys
keys = marks.keys()

#Here we have used nested loops
for i in keys:
    print("The coursed enrolled by ",i, "are as follows")
    for j in marks[i]:
        print(j)

