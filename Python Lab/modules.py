# Python modules

# 1. Write a Python program to get current time using date time function. 
'''
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
o/p
16:48:56
'''

# 2. Write a Python program to print current year, month, day using date time function. 
'''
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%Y/%m/%d")
print("Year,month,day : =", d1)

o/p:
Year,month,day : = 2021/05/03
'''


# 3. Write a Python program to print factorial of a given number using math module. 
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter number: "))
print(factorial(n))

o/p:
Enter number: 5
120
'''

# 4. Write a Python program to display Fibonacci series for 100 and 1000 using fibo module. 
'''
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter no. gerater than or equal to 0")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
   print('\n')
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

o/p:
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025
121393
196418
317811
514229
832040
1346269
2178309
3524578
5702887
9227465
14930352
24157817
39088169
63245986
102334155
165580141
267914296
433494437
701408733
1134903170
1836311903
2971215073
4807526976
7778742049
12586269025
20365011074
32951280099
53316291173
86267571272
139583862445
225851433717
365435296162
591286729879
956722026041
1548008755920
2504730781961
4052739537881
6557470319842
10610209857723
17167680177565
27777890035288
44945570212853
72723460248141
117669030460994
190392490709135
308061521170129
498454011879264
806515533049393
1304969544928657
2111485077978050
3416454622906707
5527939700884757
8944394323791464
14472334024676221
23416728348467685
37889062373143906
61305790721611591
99194853094755497
160500643816367088
259695496911122585
420196140727489673
679891637638612258
1100087778366101931
1779979416004714189
2880067194370816120
4660046610375530309
7540113804746346429
12200160415121876738
19740274219868223167
31940434634990099905
51680708854858323072
83621143489848422977
135301852344706746049
218922995834555169026
'''
# 5. Write a Python program to perform simple arithmetic operation using calc module.

'''
def add(x, y):  
    #Addition
   return x + y 
def subtract(x, y): 
    #subtraction
   return x - y 
def multiply(x, y): 
   #multiplication 
   return x * y 
def divide(x, y): 
   #divide  
   return x / y  
# take input from the user  
print("Select operation :")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")

o/p:
Select operation :
1.Add
2.Subtract
3.Multiply
4.Divide
Enter choice(1/2/3/4):3
Enter first number: 4
Enter second number: 3
4 * 3 = 12
'''
# 6. Write a Python program to generate random number between (1, 50) and to generate random character from the word “computer” using random module. 
'''
import random
randomlist = []
for i in range(1,50):
    n = random.randint(1,30)
randomlist.append(n)
print('Random no.',randomlist)

from random import shuffle
char = ['c','o','m','p','u','t','e','r']
shuffle(char)
print('Shuffled characters :',char)

o/p:
Random no. [12]
Shuffled characters : ['u', 'p', 't', 'c', 'o', 'e', 'm', 'r']
'''

# 7. Write a Python program to shuffle numbers from the given list n=[15,20 38, 45,10,5] using random module.
'''
from random import shuffle
num = [15,20,38,45,10,5]
shuffle(num)
print('Shuffled numbers :',num)

o/p:
Shuffled numbers : [45, 5, 38, 20, 10, 15]
'''