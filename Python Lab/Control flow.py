
# 1.	Python Program to check Armstrong Number
'''
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

o/p:
Enter a number: 153
153 is an Armstrong number
'''

# 2.	Python Program for Program to find area of a circle
'''
radius = int(input("Enter a radius: "))
a=3.14*r*r
print(a)

o/p:
Enter a radius: 5
78.5
'''
# 3.	Python program to print all Prime numbers in an Interval
'''
lower = 1
upper = 100
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=' ')

o/p:
Prime numbers between 1 and 100 are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
'''

# 4. Python program to check whether a number is Prime or not
'''
num=int(input('Enter any number: '))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

o/p:
Enter any number: 37
37 is a prime number
'''

# 5. Python Program for n-th Fibonacci number
'''
n = int(input("Enter number :"))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1,end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

o/p:
Enter number :10
Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34
'''

# 6.Python Program for How to check if a given number is Fibonacci number?
'''
import math
def isPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x
def isFibonacci(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)
for i in range(1,20):
    if (isFibonacci(i)==True):
        print(i," is fibonacci number")
    else:
        print(i," is not fibonnaci number")

o/p:
1  is fibonacci number
2  is fibonacci number
3  is fibonacci number
4  is not fibonnaci number
5  is fibonacci number
6  is not fibonnaci number
7  is not fibonnaci number
8  is fibonacci number
9  is not fibonnaci number
10  is not fibonnaci number
11  is not fibonnaci number
12  is not fibonnaci number
13  is fibonacci number
14  is not fibonnaci number
15  is not fibonnaci number
16  is not fibonnaci number
17  is not fibonnaci number
18  is not fibonnaci number
19  is not fibonnaci number
'''

# 7. Python Program for n\’th multiple of a number in Fibonacci Series
'''
def findPosition(k,n):
    f1=0
    f2=1
    i=2
    while(i!=0):
        f3=f1+f2
        f1=f2
        f2=f3
        if f2%k==0:
            return n*i
        i+=1
    return
n=2
k=3
print("Position of n'th multiple of k in Fibonacci series is ",findPosition(k,n))

o/p:
Position of n'th multiple of k in Fibonacci series is  8
'''



# 8.Program to find ASCII value of a character
'''
c='A'
print("The ASCII value of "+c+" is",ord(c))
Output--
The ASCII value of A is 65
'''


# 9. Program to find sum of squares of first n naturel numbers
'''
n=int(input("Enter last natural number :"))
sum=0
for i in range(1,n+1):
    sum= sum+ (i*i)
print('The sum of squares of first', n,' natural numbers is :',sum)

o/p:
Enter last natural number :10
The sum of squares of first 10  natural numbers is : 385
'''



# 10.Program to find sum of cubes of first n naturel numbers
'''
n=int(input("Enter last natural number :"))
sum=0
for i in range(1,n+1):
    sum=sum+(i*i*i)
print("The sum of first",n, "natural numbers is :",sum)

o/p:
Enter last natural number :10
The sum of first 10 natural numbers is : 3025
'''

# 11 Pattern 1
'''
rows =int(input('Enter no. of rows: '))
for num in range(rows+1):
    for i in range(num):
        print(num, end='')
    print('')

o/p:
Enter no. of rows: 5

1
22
333
4444
55555
'''
# 11 Pattern 2 
'''
rows =int(input('Enter no. of rows: '))
for i in range(rows):
    for j in range(rows):
        if j==0 or i==(rows-1) or i==j:
            print('*', end='')
        else:
            print(end=' ')
    print()

 o/p:
 Enter no. of rows: 5
*    
**
* *
*  *
*****
'''


# 11 Pattern 3 
'''
rows =int(input('Enter no. of rows: '))
for i in range(rows):
    for j in range(rows):
        if j==(rows-1) or i==0 or i==j:
            print('*', end='')
        else:
            print(end=' ')
    print()

o/p:
Enter no. of rows: 5
*****
 *  *
  * *
   **
    *
'''

# 11 Pattern 4
'''
str = input('Enter the string :')
for i, char in enumerate(str):
    print(str[0:i+1])

o/p:
Enter the string :Python
P
Py
Pyt
Pyth
Pytho
Python
'''

# 11 Pattern 5
'''
rows =int(input('Enter no. of rows: '))
for i in range(rows,0,-1):
    n=i
    for j in range(0,i):
        print(n,end='')
    print('\r')

o/p:
Enter no. of rows: 5
55555
4444
333
22
1
'''

# 11 Pattern 6
'''
rows =int(input('Enter no. of rows: '))
c=1 
s=2
for i in range(rows):
    for j in range(1,s):
        print(c,end=' ')
        c+=1
    print('')
    s+=1

o/p:
Enter no. of rows: 5
1 
2 3
4 5 6
7 8 9 10 
11 12 13 14 15
'''

# 11 Pattern
'''
for i in range(rows):
    for j in range(rows-i):
        print(' ', end='')
    for j in range(2*i+1):
        if j==0 or j==2*i or i==rows-1:
            print('*',end='')
        else:
            print(' ', end='')
    print()

o/p:
Enter no. of rows: 5
     *
    * *
   *   *
  *     *
 *********
 '''