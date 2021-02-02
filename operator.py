number=5
# number % 2==0
if number & 1==0:
    print('even')
else:
    print('odd') #will print it

number=2
if number & 1==0:
    print('even') #will print it
else:
    print('odd')

name='sumit'
if name=='sumit':
    print(name.upper()) #will print SUMIT

name='Sumit'
if name=='sumit':
    print(name.upper()) 
else:
    print(name) #will print Sumit

# = equal to means we assign value to variable (Assignment operator)
# == check, a variable is equal to another(equality operator)

name = 'sumit'
if name =='saket':
    print(name)   #name is not equal to saket so print sumit

# for inequality != 
if name != 'saket':
    print('true')  #true because name = sumit

age =24
if age ==24:
    print('true') #true because age =24

age =24
if age !=24:
    print('true') 
else:
    print('false') #false because age = 24 

age = 18
if age >=18:
    print('Able to vote') #will print for 18 or greater than it
else:
    print('unable to vote')

age = 18
if age > 18:
    print('Able to vote') 
else:
    print('unable to vote') #will print for greater than 18 only

# and operator
# and for all test cases if one false all false all
age=18 
if age >=10 and age <=20:
    print('Age between 10 to 20') # print Age between 10 to 20

age=28 
if age >=10 and age <=20:
    print('Age between 10 to 20') 
else:
    print('not satisfying condition') #print  not satisfying condition