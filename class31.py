#Tuple...
#A Tuple is a an ordered , immutable collection.
# Once you create it, you cant change add or
# remove items

#.1 Annoted by (paranthesis)
#.2 Tuple Ordered -> their are indexes
#.3 Hetrogenous -> Mixed types values are allowes
#.4 Duplicate Elements are alowed 
#.5 Immutable
#.6 We can do slicing 

'''t = () #Empty Tuple
print(type(t))'''

#METHODS 
#1 . .COUNT () -> count the occurence of any value 
#2. .INDEX() -> Show the index location of the 
# first occuring element.

'''t = (1,2,1,2,1)
print(t.count(1))
print(t.index(2))'''


#OPERATIONS 
# + -> Two tuples can concatenate 
# * -> Repetition
'''t1 = (1, 2)
t2 = (3, 4)
print (t1 + t2)
print (t1 * 5)'''

t = (1,2,[2,3,4])
t[2].append(100)
print(t)