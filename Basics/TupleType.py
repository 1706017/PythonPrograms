"""
Author : Amrit Manash
Created On : 20th Jan 2023

"""
#Tuple is a collection type in python that can use to store multiple values of diff types
#The only diff between tuple and list is that list is mutable that is which can be modified but a tuple is immutable that is
#tuple cannot be modified

#tuple can hold duplicates
#tuple reserve the order in which element is put inside the tuple

mytpl = (12,13,26,'Amrit',12)
print(mytpl)

#if there is a single element in a tuple just assign one comma at the end other wise it will be treated as normal primitive type
myNewtpl = (23)
print(type(myNewtpl)) # Here you can see that you will get type as int

mytuple = (23,)
print(type(mytuple)) #Here you will get type as tuple as you have used , with single value inside ()

#Some Important tuple method in tuple
#1.count() : it is used to count the number of times a value is there inside a tuple
print(mytpl)
print(mytpl.count(12))

#2.index() : it is used to return the index of particular value in a tuple so if there are multiple values in a tuple
#then first occurence index will be returned
print(mytpl.index(12))

#you can also use multiple methods from the list that do not modifies a tuple like min(),max()




