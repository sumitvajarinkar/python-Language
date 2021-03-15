# List

# 1.  Write a Python program to sum all the items in a list. 
'''
nums=[1,2,3,4,5]
s=0
for i in nums:
    s+=i
print(s)

o/p:
15
'''

# 2. Write a Python program to multiplies all the items in a list. 
'''
nums=[1,2,3,4,5]
s=1
for i in nums:
    s*=i
print(s)

o/p:
120
'''

#  3. Write a Python program to get the largest number from a list. 
'''
nums=[25,464,32,79]
l=nums[0]
for i in nums:
    if i>l:
        l=i
print(l)

o/p:
464
'''
#  4. Write a Python program to get the smallest number from a list
'''
nums = [25,464,32,79]
s = nums[0]
for i in nums:
    if i < s :
        s = i
print(s)

o/p:
25
'''

# 5.Python program to count the number of strings where the string length is 2 or more and the
# first and last character are same from a given list of strings.
'''
def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))
o/p:
2
'''


# 6.Write a Python program to get a list, sorted in increasing order by the last element in each tuple
# from a given list of non-empty tuples.
'''
def last(n):
    return n[-1]
def sort(tuples):
    return sorted(tuples,key=last)
a=[(1,3),(3,2),(2,1)]
print("sorted:", sort(a))

o/p:
sorted: [(2, 1), (3, 2), (1, 3)]
'''


# 7.Python program to remove duplicates from a list.
'''
duplicate=[2,3,4,5,6,7,34,5,6,2,445,66,66]
print(list(set(duplicate)))

o/p
[2, 3, 4, 5, 6, 7, 34, 66, 445]
'''


# 8.Python program to check a list is empty or not.
'''
a=[6,7]
if len(a)==0:
    print("List is empty")
else:
    print("List is not empty")

o/p:
List is not empty
'''


# 9.Python program to clone or copy a list.
'''
def cloning(list1):
    list_cpy=list(list1)
    return list_cpy
list1=[2,3,4,7,67,45,93,23]
list2=cloning(list1)
print("Original list: " ,list1)
print("Copied list: ", list2)

o/p:
Original list:  [2, 3, 4, 7, 67, 45, 93, 23]
Copied list:  [2, 3, 4, 7, 67, 45, 93, 23]
'''


# 10.Python program to find the list of words that are longer than n from a given list of words.
'''
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

o/p:
['quick', 'brown', 'jumps', 'over', 'lazy']
'''

#Dictionary

# 1.Python script to add a key to a dictionary.
'''
a={1:'Amit',2:'Saurabh', 3:'Shreyas'}
print(a)
a.update({4:'Prajwal'})
print(a)

o/p:
{1: 'Amit', 2: 'Saurabh', 3: 'Shreyas'}
{1: 'Amit', 2: 'Saurabh', 3: 'Shreyas', 4: 'Prajwal'}
'''


# 2.Python script to concatenate following dictionaries to create a new one.
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

o/p:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''


# 3.Python script to check whether a given key already exists in a dictionary.
'''
d={'A':1,'B':2,'C':3}
key=input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")

o/p:
Enter key to check:A
Key is present and value of the key is:
1
'''

# 4.Python program to iterate over dictionaries using for loops.
'''
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])

o/p:
Red corresponds to  1
Green corresponds to  2
Blue corresponds to  3
'''

# Tuples:

# 1. Write a Python program to create a tuple with different data types.  
'''
t = 1910033, 'csit','$',3.14
print(t)

o/p:
(1910033, 'csit', '$', 3.14)
'''

# 2. Write a Python program to create a tuple with numbers and print one item.  
'''
t = 25,464,32,79
print(t)
t = 32,
print(t)

o/p:
(25, 464, 32, 79)
(32,)
'''
# 3.   Write a Python program to find the repeated items of a tuple.
'''
t=1,2,2,3,4,5,3,3,5
c=t.count(3)
print(c)

o/p:
3
'''
# 4. Write a Python program to add an item in a tuple.  
'''
t=10,20,30,40,50
print(t)
t=t+(60,)
print(t)

o/p:
# (10, 20, 30, 40, 50)
# (10, 20, 30, 40, 50, 60)
'''

# 5. Write a Python program to convert a tuple to a string. 
'''
t='a','b','c','d'
str=''.join(t)
print(str)

o/p:
abcd
'''

# Sets:
# 1. Write a Python program to iterate over sets. 
'''
names={'rahul', 'neha', 'sham', 'ram'} 
for i in names:
    print(i)

o/p:
ram
neha
rahul
sham
'''
# 2. Write a Python program to add member(s) in a set.
'''
names={'rahul', 'neha', 'sham', 'ram'} 
names.add('raj')
print(names)

o/p:
{'neha', 'ram', 'rahul', 'sham', 'raj'}
'''

# 3. Write a Python program to create an intersection of sets.
'''
set_a = {'rahul', 'neha', 'sham'}
set_b = { 'sham', 'raj'}
set_c = set_a & set_b
print(set_c)

o/p:
{'sham'}
'''

# 4. Write a Python program to create a union of sets.  
'''
set_a = {'rahul', 'neha', 'sham'}
set_b = { 'sham', 'raj'}
set_c = set_a | set_b
print(set_c)

o/p:
{'rahul', 'raj', 'neha', 'sham'}
'''
# 5. Write a Python program to create set difference.  
'''
set_a = {'rahul', 'neha', 'sham'}
set_b = { 'sham', 'raj'}
set_c = set_a - set_b
print(set_c)

o/p:
{'neha', 'rahul'}
'''

# 6. Write a Python program to create a symmetric difference. 
'''
set_a = {'rahul', 'neha', 'sham'}
set_b = { 'sham', 'raj'}
set_c = set_a ^ set_b
print(set_c)

o/p:
{'neha', 'rahul', 'raj'}
'''