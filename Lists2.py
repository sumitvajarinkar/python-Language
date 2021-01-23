
names=['Sumit', 'saket', 'Avni','pruthvi']
print(names) #['Sumit', 'saket', 'Avni', 'pruthvi']

# removing last element by del and pop
#when dont want any element use del
#when you want to move element use pop
del names[-1]
print(names) #['Sumit', 'saket', 'Avni']

del names[len(names)-1]
print(names) #['Sumit', 'saket']

del names[0]
print(names) #['saket']

popped=names.pop()
print(popped) #saket
print(names) #[]

names=['Sumit', 'saket', 'Avni','pruthvi']
popped=names.pop(2)
print(popped) #Avni

#Remove by value
names=['Sumit', 'saket', 'Avni','pruthvi']
names.remove('Sumit')
print(names) #['saket', 'Avni', 'pruthvi']

#Remove on  duplicate? 
#Removes 1st insatnce of element
names=['Sumit', 'saket', 'Avni','pruthvi','saket']
names.remove('saket')
print(names)     #['Sumit', 'Avni', 'pruthvi', 'saket']

#if want to delete all duplicate
names.remove('saket')
print(names)    #['Sumit', 'Avni', 'pruthvi']

#organizing a list
#sorting- ascending(increasing), dscending(decreasing)

#increasing
names.sort()
print(names) #['Avni', 'Sumit', 'pruthvi']

#so here as we have ASCII value from 67 for A 96 for a so A will come first
names=['Sumit', 'Sumi', 'Avni','aruthvi']
names.sort()
print(names) #['Avni', 'Sumi', 'Sumit', 'aruthvi']

#decreasing order
names.sort(reverse = True)
print(names) #['aruthvi', 'Sumit', 'Sumi', 'Avni']

numbers=[8, 2, 9, 1]
numbers.sort()
print(numbers) #[1, 2, 8, 9]
numbers.sort(reverse=True)
print(numbers) #[9, 8, 2, 1]

#for temporary save it different variable
#or use sorted()
numbers=[3, 9, 5, 1]
print(sorted(numbers)) #[1, 3, 5, 9]
print(numbers) #[3, 9, 5, 1]

#reverse
names=['Sumit', 'Sumi', 'Avni','aruthvi']
names.reverse()
print(names) #['aruthvi', 'Avni', 'Sumi', 'Sumit']

numbers.reverse()
print(numbers) #[1, 5, 9, 3]

numbers.reverse()
print(numbers) #[3, 9, 5, 1]

#avoid index errors when working with lists