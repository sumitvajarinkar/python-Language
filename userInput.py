#input by default takes Strings 

# string input
name=input('Enter your name: ')#sumit
print(name) #sumit
print(type(name)) #<class

# int input
name=int(input('Enter any number: '))#56
print(name) #56
print(type(name)) #<class 'int'>

# float input
name=float(input('Enter any number: '))#8.9 
print(name) #8.9
print(type(name)) #<class 'float'>

number=input('Enter a nummber: ') #4
number=float(number)
number+=1
print(number) #5.0
print(type(number)) #<class 'float'>

# List
numbers=(input('Enter the Numbers:')).split() #1 2 3 4
print(numbers) #['1', '2', '3', '4']
print(type(numbers)) #<class 'list'>

# what is split ?
# it separate each element with space
