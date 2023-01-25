s="you are awesome"
snew="""
you are the creator
of your 
Destiny
"""
print(s)
print(snew)

#String indexing to reach directly to charcters in a string
print(s[0])

#String repetation using * symbol
print(s*2)

#String slicing
print(s[0:5]) #it will start from 0 and will print upto index 4 exlude index 5
print(s[0:])
print(s[:7])
print(s[-5:-1]) #here -1 means the last character of string

#steps size in string slicing
print(s[0:9:2])


#String methods
#1. strip : to remove the leading spaces from strings from both sides left and right
s2=" you are a good boy "
print(s2)
print(s2.strip())
print(s2.lstrip()) #to remove space from left
print(s2.rstrip()) #to remove space from right

#2.find : it returns the index value of substring from which it starts in a string
print(s.find("are"))

#3.count : it is used to return the number of times a substring appears in a string
print(s.count("a"))

#4.replace : it is used to replace the old substring with a new substring in a string
print(s.replace("awesome","super")) #Here the first param is old value and second param is new value

#5.lower() : to convert string to lowercase
print(s.lower())

#6.upper() : to convert string to uppercase
print(s.upper())

#7.title() : to convert the string into title
print(s.title())



