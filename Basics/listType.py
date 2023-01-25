"""
Author : Amrit Manash
Created On : 20th Jan 2023

"""



#List is a collection in python that is used to hold multiple values
#values can be of different types

myList = [17,'Amrit',25,35500.23]

print(myList)

#List indexing
print(myList[1])

#List slicing
print(myList[1:3])

#List repetation
print(myList*4)

#Some Important List methods

#1.append() : it is used to add element in last of a list
myList.append('Bhagalpur')
print(myList)

#2.remove() : it is used to remove value from a list so we directly pass the value from list that will be removed
myList.remove(25)
print(myList)

#3.del(myList) : it will delete list element by index value
del(myList[3])
print(myList)

#4.clear() : it is used to empty the list
myList.clear()
print(myList)

#5.min() : it is used to find the minimum element in a list
newList = [12,13,21,45,-1,-8,56,89,23]
print(min(newList))

#6.max() : it is used to find the maximum element in a list
print(max(newList))

#7.insert() : it is used to insert element in a list at a particular index
newList.insert(0,'Amrit')
print(newList)

#8.sort() : it is used to sort list in either ascending or descending order
numList = [12,23,78,10,9]
numList.sort()  #This will sort the list in ascending order
print(numList)

numList.sort(reverse=True) #This will sort the list in descending order
print(numList)






