#LISTS the array form as in JS

mylist = ['a', 'b', 'c', 'd', 'e', 'f']
print(mylist)

#lists work with objects
mylistobject = ['abcdefg', 1, 2, 3, 4, True, [1,2,3]]
print(mylistobject)

#getting the size of list
print(len(mylistobject))


print('before reassignment')
print(mylist)

mylist[0] = 'NEW ITEM' #reassigning a new item to the list
print("after reassignment:")
print(mylist)

#APPEND METHOD
## append a new item to the end of the list.
mylist2 = ['a', 'b', 'c', 'd', 'e', 'f']
listappended = ["NEW ITEM1", "NEW ITEM2"]
mylist2.append(listappended)
print(mylist2)

#EXTEND METHOD
## extend the currently list with the extended list.
mylist3 = ['a', 'b', 'c', 'd', 'e', 'f']
listtwo = ["x", 'y', 'z']
mylist3.extend(listtwo)
print(mylist3)

# POP METHOD
## pops (takes of) the last item of your list. Though you can add the index to pop other letters instead of the last.
mylistpop = ['a', 'b', 'c', 'd', 'e', 'f']
item = mylistpop.pop()
print(mylistpop) #without 'f'
print(item) 

firstitem = mylistpop.pop(0)
print(mylistpop) #without 'a' and 'f'
print(firstitem)

# REVERSE
## reverse the order of the list
mylistreverse = ['a', 'b', 'c', 'd', 'e', 'f']
mylistreverse.reverse()
print(mylistreverse)

# SORT
# sort the order of the list
mylistsort = [33, 1, 24, 109, 4, 87]
mylistsort.sort()
print(mylistsort)

# INDEX NESTED LIST
## use two sets of brackets to the nested, if there are more nested lists inside the nested, use other brackets.
mylistnested = [1,2,['x','y','z']]
print(mylistnested[2][1]) #should print 'y'

#LIST COMPREHENSION
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[0][0])

## this is the list comprehension method
first_col = [row[0] for row in matrix] #defining the variable name row, first getting the first element, and row is in the matrix, which is each element.
print(first_col)