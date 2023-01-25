"""
Author : Amrit Manash
Created On : 20th Jan 2023

"""

#Set is a collection type in python that contains multiple value
#Set does not allow duplicates it will simply ignore duplicates
#Set does not maintain the order in which elements where added to a set
#Sets are mutable that means element of a set can be modified

mySet = {12,12,'Amrit','Manash',35000}
print(type(mySet))
print(mySet)

#Sets do not allow for indexing , slicing and repeation

#to add elements in a set we use method update()
mySet.update([46,90,78])
print(mySet)

#we can also remove the element from a set using remove()
mySet.remove(12)
print(mySet)


