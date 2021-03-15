# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:12:59 2021

@author: user
"""

# 1 Python program to add two numbers
'''
n1=int(input('Enter a number :\n'))
n2=int(input('Enter another number :\n'))
sum=n1+n2
print(f'Addition of {n1} and {n2} is {sum}')

o/p:
Enter a number :1324
Enter another number :213
Addition of 1324 and 213 is 1537
'''


# 2 Maximum of two numbers in Python
'''
n1=int(input('Enter a number :\n'))
n2=int(input('Enter another number :\n'))
if n1>n2:
    print(f'{n1} is Maximum number')
print(f'{n2} is Maximum number')

Enter a number :2

Enter another number :3
3 is Maximum number
'''

# 3 Python Program for factorial of a number
'''
n1=int(input('Enter a number :\n'))
fact=1
for i in range(1,n1+1):
    fact*=i
print(f'Factorial of {n1} is :{fact}')

o/p:
    Enter a number :
5
Factorial of 5 is :120
'''

# 4 Python Program for simple interest
'''
p=float(input('Enter initial principal balance :\n'))
r=float(input('Enter interest rate :\n'))
t=float(input('Enter number of time periods elapsed :\n'))
SI = ((p*r*t)/100)
print(f'{SI} is Simple interest')

o/p:
    Enter initial principal balance :
1

Enter interest rate :
2

Enter number of time periods elapsed :
3
0.06 is Simple interest
'''

# 5 Python Program for compound interest
'''
p=float(input('Enter initial principal balance :\n'))
r=float(input('Enter interest rate :\n'))
t=float(input('Enter number of time periods elapsed :\n'))
#n=(input('Enter number of times interest applied per time period :\n'))
CI = p*(pow(1+r/100,t))
print(f'{CI} is compound interest')

o/p:
    Enter initial principal balance :
1

Enter interest rate :
2

Enter number of time periods elapsed :
3
1.0612080000000002 is compound interest
'''

# 6 To perform and display addition, subtraction, division, multiplication of three numbers.
'''
n1=int(input('Enter a number :\n'))
n2=int(input('Enter another number :\n'))
n3=int(input('Enter another one number :\n'))
a=n1+n2+n3
print(f'Addition of {n1}, {n2} and {n3} are :{a}\n')
s=n1-n2-n3
print(f'Subtraction of {n1}, {n2} and {n3} are :{s}\n')
m=n1*n2*n3
print(f'Multiplication of {n1}, {n2} and {n3} are :{m}\n')
d=n1/n2/n3
print(f'Division of {n1}, {n2} and {n3} are :{d}\n')

Enter a number :
9

Enter another number :
6

Enter another one number :
3
Addition of 9, 6 and 3 are :18

Subtraction of 9, 6 and 3 are :0

Multiplication of 9, 6 and 3 are :162

Division of 9, 6 and 3 are :0.5
'''

# 7 To find the average of three numbers.
'''
n1=int(input('Enter a number :\n'))
n2=int(input('Enter another number :\n'))
n3=int(input('Enter another one number :\n'))
s=n1+n2+n3
avg=s/3
print(f'The average of {n1},{n2},{n3} numbers is {avg}')

o/p:
    Enter a number :
1

Enter another number :
2

Enter another one number :
3
The average of 1,2,3 numbers is 2.0
'''

# 8 Implement program to find the area of circle.
'''
r=int(input('Enter a radius of circle :\n'))
area=3.14*r*r
print(f'Area of cicle is : {area}')

o/p:
    Enter a radius of circle :
5
Area of cicle is : 78.5
'''

# 9 Implement program to find the area of triangle.
'''
b=int(input('Enter a base :\n'))
h=int(input('Enter a height :\n'))
area=0.5*b*h
print(f'Area of triangle is : {area}')

o/p:
    Enter a base :
3

Enter a height :
4
Area of triangle is : 6.0
'''

# 10 Implement the program to calculate the monthly Milk bill of customer 
#(based on no. of liter the Milk taken by customer and amount per liter) calculate for 30 Days
'''
no_of_milk=float(input('Enter how many litres of milk customer purchase for a month :\n'))
amount=float(input('Enter the amount of milk per litre :\n'))
bill=no_of_milk*amount*30
print(f'Bill of customer for 30 days {bill}')

o/p:
    Enter how many litres of milk customer purchase for a month :
25.5

Enter the amount of milk per litre :
50
Bill of customer for 30 days 38250.0
'''

# 11 Implement the to find the gross salary of an employee.
#Take basic from user
#DA is 80% and TA is 20 %
'''
s=int(input('Enter a salary :\n'))
gross_salary=0.8*0.2*s
print(f'Gross salary is :{gross_salary}')

o/p:
    Enter a salary :
50000
Gross salary is :8000.000000000002
    '''