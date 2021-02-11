current_number=1
while current_number <=5:      #conditional sattement
        print(current_number)
        current_number+=1       #increment
# 1
# 2
# 3
# 4
# 5

message=''
while message !='quit':
        message=input('Enter a message: ')
        print(message) #if you type quit then it will out of loop

message=''
flag=True
while flag:  #flag true
        message=input('Enter a message: ')
        if message == 'quit':
                flag=False  #flag false
        else: 
                print(message) #if you type quit then it will out of loop

# check if all numbers are even or not

numbers =input('Enter the numbers: ')
flag=True
for number in numbers.split():
        if int(number) & 1 != 0: # number%2 != 0 (gives odd)
                flag= False      #we get odd, condition false
if flag:
        print('All numbers are even')
else:
        print('All numbers are not even')

s='1 2 3'
print(s.split()) #['1', '2', '3']

# break to exit loop 

numbers =input('Enter the numbers: ')
flag=True
# ['1', '2', '3']
for number in numbers.split():
        print(number)
        if int(number) & 1 != 0: # number%2 != 0 (gives odd)
                flag= False      #we get odd, condition false
                break            #when we get odd we break loop
if flag:
        print('All numbers are even')
else:
        print('All numbers are not even')
# Enter the numbers: 1 2 3
# All numbers are not even

message=''
while True:  #flag true
        message=input('Enter a message: ')
        if message == 'quit':
                break  #break out of loop
        else: 
                print(message) #if you type quit then it will out of loop


# continue

while True:
        number =input('Enter a number: ')
        if number == 'quit':
                break
        number=int(number)
        if number & 1 !=0:
                continue     #goes to begin ofloop again
        print(number)        #if number is even then it will print


# avoid infinite loop
# while True:
#         print('Hi...')
# RUN for infinite times

# using while with lists
numbers=[]
while True:
        number=input('Enter a number, or quit when done! ')
        if number =='quit':
                break
        else:
                numbers.append(int(number))     #modifying list
print(numbers) #[2, 42, 12, 1, 22, 334, 21]

# while with remove()

numbers=[1, 2, 3, 1, 5, 1]
numbers.remove(1)
print(numbers) #[2, 3, 1, 5, 1]

numbers=[1, 2, 3, 1, 5, 1]
while 1 in numbers:
          print(numbers)
          numbers.remove(1)
print(numbers) 
# [1, 2, 3, 1, 5, 1]
# [2, 3, 1, 5, 1]
# [2, 3, 5, 1]
# [2, 3, 5]

# Dictionary
responses={}
while True:
        country=input("Enter a Country name ")
        capital=input("Enter the Capital ")
        responses[country]=capital
        repeat=input("Would you like to add more country/capital? (yes/no) ")
        if(repeat=='no'):
                break
for country, capital in responses.items():
        print(f'country={country}, capital={capital}')
# Enter a Country name India
# Enter the Capital New Delhi
# Would you like to add more country/capital? (yes/no) yes
# Enter a Country name Uk
# Enter the Capital London
# Would you like to add more country/capital? (yes/no) no
# country=India, capital=New Delhi
# country=Uk, capital=London