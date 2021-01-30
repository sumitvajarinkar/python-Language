for value in range(1,5):
    print(value) #5 will not print (n-1)
# to print any number till n then (m,n+1)
numbers = list(range(1,5))
print(numbers) #[1, 2, 3, 4]

numbers = list(range(1,11,2)) #skip by 2 difference with (n-1)
print(numbers) #[1, 3, 5, 7, 9]

numbers = list(range(1,11,3)) #skip by 2 difference with (n-1)
print(numbers) #[1, 4, 7, 10]

output =[]
for value in range(1,11): #1 to 10
    num=5*value #multiply
    output.append(num) #append all together
print(output) #[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# maths

numbers=list(range(1,8,2))
print(numbers) #[1, 3, 5, 7]
print(min(numbers)) #min no. in list 1
print(max(numbers)) #max no. in list 7
print(sum(numbers)) #sum is 16

# inilne table of 5
output=[5*value for value in range(1,11)]
print(output) #[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Multiple list elements at one global
# slice

numbers=[1,2,3,4]
# keep in mind index of numbers
print(numbers[1:3]) #[2, 3] index from 1 to 2 [2, 3]
print(numbers[0:4]) #[1, 2, 3, 4] index from 0 to 3 [1, 2, 3, 4]
print(numbers[2:3]) #[3] index from 2 to 3 so its only print 2 [3]
print(numbers[2:2]) #[] index from 2 to 2 so will not print any []
print(numbers[2:1]) #[] index from 2 to 1 so will not print any []
print(numbers[:3]) #[] index from start 0 to 2 access from starting [1, 2, 3]
print(numbers[1:]) #[] index from 1 to end access from starting [2, 3, 4]
print(numbers[-2:]) #[] -2 print last 2  [3, 4]
print(numbers[:-3]) #[] -3 print 1st [1]

for number in numbers[:3]:
    print(number) #1 2 3 4

# copy
numbers_copy=numbers[:] #start from 0 to end
numbers.append(5)
numbers_copy.append(6)
print(numbers) #[1, 2, 3, 4, 5]
print(numbers_copy) #[1, 2, 3, 4, 6]