# or operator
# or for all test cases false all then it willl falls

age=28 
if age >=10 or age <=20:
    print('Age between 10 to 20') #will print it
else:
    print('not satisfying condition')

names=['saket','shubham','neha']
print('saket' in names) #True
print('Saket' in names) #False

if 'neha' in names:
    print('yes') #will print it
else:
    print('no')

# use of not
if 'raju' not in names:
    print('no') #will print it
else:
    print('yes') 

# boolean expression 0/1 true/false
sumit = 1
if sumit:
    print('YES') #will print it
    print('sumit')#will print it
else:
    print('NO')

sumit = 0
if sumit:
    print('YES')
else:
    print('NO') #will print it
    print('No sumit')#will print it

# IF-ELIF
marks= 70
if marks >= 90 or marks <= 100:
    print('Grade A') #will print it
elif marks >= 70 or marks <90:
    print('Grade B')
elif marks >=50 or marks < 70:
        print('Grade C')
elif marks >=30 or marks < 0:
        print('Grade D')
else:
    print('fail')

marks= 40
if marks >= 90 and marks <= 100:
    print('Grade A')
elif marks >= 70 and marks <90:
    print('Grade B')
elif marks >=50 and marks < 70:
        print('Grade C')
elif marks >=30 and marks < 50:
        print('Grade D') #will print it
else:
    print('fail')

marks=70
if marks >=90:
    print('A')
elif marks >=70:
    print('B')
elif marks >=50:
    print('C')
else:
    print('fail')


names=['sumit','saket','neha']
if 'sumit' in names:
    print('sumit')
elif 'saket' in names:
    print('saket')

numbers = [2,3,5,8]
for number in numbers:
    if number%2 ==0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')
# 2 is even
# 3 is odd
# 5 is odd
# 8 is even

# empty
numbers=[]
if numbers:
    print('list is not empty')
else:
    print('list is empty') #will print it

numbers=[1,2]
if numbers:
    print('list is not empty') #will print it
else:
    print('list is empty')  