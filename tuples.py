# list vs tuple

numbers=[1,2,3]
numbers[0]=5
print(numbers)
# [5, 2, 3]

# Lists : have [] square brackets
#     -Items in a list can be modified
#     -Lists are Mutable
# Data structure which similar to lists but that cannot be modified ?
# So, we use Tuple :have () round brackets

origin = (0,0)
# origin[0]=1 TypeError: 'tuple' object does not support item assignment

# without () round brackets it also tuple
origin = 0,0
print(type(origin)) #<class 'tuple'>

# Is it tuple - No !
origin_x, origin_y=0,0
print(type(origin_x)),print(type(origin_y))
# <class 'int'>
# <class 'int'>

# For simplicity use round brackets to Show Tuple

# for single element as tuple
x=(1, )
print(type(x)) #<class 'tuple'>

# Looping through tuple elements
numbers=(1,2,3,4,5)
for number in numbers:
    print(number)
# 1
# 2
# 3
# 4
# 5

# over write a tuple
origin_x=(0,0)
origin_y=(1,1)
print(origin_y) #(1, 1)

# Inserting in Tuple

numbers=(1,2,3,4,5)
print(numbers)
numbers=numbers + (6,7,8,9) # append
print(numbers) #(1, 2, 3, 4, 5, 6, 7, 8, 9)

numbers=(1,2,3,4,5)
print(numbers)
numbers=(6,7,8,9) + numbers # append
print(numbers) #(6, 7, 8, 9, 1, 2, 3, 4, 5)

# operation similar to lists
# negative indexing
# slicing
# min, max, sum function
# len()

# insert, delete not work
