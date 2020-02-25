#Basics
'hello'
"hello"

# 'I'm a dog # not work
"I'm a dog" #work

#INDEXING (getting one letter of the string)
mystring = 'abcdefg'
print(mystring[0])

#SLICING (getting part of the string)
print(mystring[4:]) #starting from 4 going to the end
print(mystring[:3]) #starting from 0 going to 2 -python doesn't include the last
print(mystring[::2]) #gets the whole string stepsizing 2 by 2

#BASIC METHODS
x = mystring.upper() #uppercase string
print(x)

y = x.lower() #lowercase
print(y)

cap = mystring.capitalize() #capitalize the string
print(cap)

my2string = 'Hello World'
z = my2string.split() #split the word 
print(z)

#PRINT FORMATING
f = "Insert another string here: {}".format("INSERT ME") #inserting text inside other string
print(f)

g = "Item 1: {x} Item 2: {y}".format(x="cat", y="dog") #for multiple printing formating uses the double quotes.
print(g)

