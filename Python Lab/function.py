# 5.1 Write a Python function to find the Max of three numbers.
'''
def maximum(a, b, c): 
   num = [a, b, c] 
   return max(num)  
x = int(input("Enter First number "))
y = int(input("Enter Second number "))
z = int(input("Enter Third number "))
print(f'Maximum Number is {maximum(x, y, z)}') 

o/p:
Enter First number 243
Enter Second number 21326
Enter Third number 653      
Maximum Number is 21326
'''

# 5.2 Write a Python function to sum all the numbers in a list. Sample List : (8, 2, 3, 0, 7)
'''
def sum(nums):
    s=0
    for i in nums:
        s+=i
    print(s)
nums=[8, 2, 3, 0, 7]
sum(nums)

o/p:
20
'''
# 5.3 Write a Python function to multiply all the numbers in a list. Sample List : (8, 2, 3, -1, 7)
'''
def mul(nums):
    m=1
    for i in nums:
        m*=i
    print(m)
nums=[8, 2, 3, -1, 7]
mul(nums)
o/p:
-336
'''

# 5.4 Write a Python program to reverse a string.  
'''
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
s='python'
print(f'{reverse(s)}')

o/p:
nohtyp
'''

# 5.5 Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=int(input('Enter a number :\n'))
print(factorial(n))
o/p:
Enter a number :
5 
120
'''

# 5.6 Write a Python function to check whether a number is in a given range.
'''
def inrange(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
inrange(7)
o/p:
 7 is in the range
 '''

#  5.7 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
'''
def upperlower(s):
    l,u = 0,0
    for i in s: 
        if (i>='a'and i<='z'): 
            l=l+1                 
        if (i>='A'and i<='Z'): 
             u=u+1   
    print('Lower case characters: ',l) 
    print('Upper case characters: ',u) 
s=input('Enter a string ')
upperlower(s)
o/p:
Enter a string SuMiT
Lower case characters:  2
Upper case characters:  3
'''

# 5.8 Write a Python function that takes a list and returns a new list with unique elements of the first list
'''
def noduplicate(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(noduplicate([1,2,3,3,3,3,4,5])) 

o/p:
[1, 2, 3, 4, 5]
'''

# 5.9 Write a Python program to print the even numbers from a given list.                                       
'''
def even(nums):
    for i in nums: 
        if i % 2 == 0:
            print(i, end = " ") 
nums= [12,34,131,567,22,56]
even(nums)

o/p:
12 34 22 56 
'''

# 5.10 Write a Python program to detect the number of local variables declared in a function.
# used co_nlocals() function 
'''
def fun(): 
    a = 1
    b ='z'
    str = 'GeeksForGeeks'

print(fun.__code__.co_nlocals) 
o/p:
3
'''