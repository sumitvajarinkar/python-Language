# A list is a collection of items in a particular order
# give name to lits in plural i.e. names,games,etc.

names=['Sumit', 'saket', 'Avni']
print(names)

# Lists are ordered, position/index starts with 0

print(names[0]) #prints Sumit
print(names[1]) #prints Saket
print(names[2]) #prints Avni

print(names[0].upper())
print(names[1].title()) #makes 1st char UPPERCASE

# we can store different data types in Lists
random_lists = ['sumit', 1, 3.232]
print(random_lists)

# also store lists in lists
lists_in_lists=['sumit',['Avni',1,2.899]]
print(lists_in_lists)

#print last element
length=len(names)
print(names[length-1]) #index starts from 0

# negative index for last element
print(names[-1]) #3rd/last element
print(names[-2]) #2nd last
print(names[-3]) #1st element
# print(names[-4]) list index out error

message='hello world'
print(message[0]) #print h
print(message[-1]) #print d

# message[0]='H' cant assign in string
message='Hello world'
print(message)

# you can replace in Lists by asssigning
names[0]='Vajarinkar'
print(names)

# Mutable(value can be changed) e.g Lists
# immutable(cant assign value but can override by assigning in diff variable) e.g. strings

# Operations in Lists

# inserting element 
# at end
names.append('connected') #insert at end
print(names)

#specific position
names.insert(2,'pruthvi') #['Vajarinkar', 'saket', 'pruthvi', 'Avni', 'connected']
print(names)
names.insert(len(names),'Raj') #['Vajarinkar', 'saket', 'pruthvi', 'Avni', 'connected', 'Raj']
print(names)
#negative indexing
names.insert(-1,'insert 2nd last') #['Vajarinkar', 'saket', 'pruthvi', 'Avni', 'connected', 'insert 2nd last', 'Raj']
print(names)
