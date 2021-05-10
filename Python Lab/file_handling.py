#Python file handling

# 1. Write a Python program to read an entire text file. 
'''
def file_read(fname):
        txt = open(fname)
        print(txt.read())
file_read('1910033.txt')

o/p:
Name : Sumit Vajarinkar
Branch : CSIT
PRN : 1910033
'''

#  2. Write a Python program to read first n lines of a file. 
'''
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('1910033.txt',2)

o/p:
Name : Sumit Vajarinkar

Branch : CSIT
'''

#  3. Write a Python program to append text to a file and display the text. 
'''
def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("I am from RIT\n")
                myfile.write("21 yrs. old")
        txt = open(fname)
        print(txt.read())
file_read('1910033.txt')

o/p:
I am from RIT
21 yrs. old
'''

#  4. Write a Python program to read last n lines of a file. 
'''
import sys
import os
def file_read_from_tail(fname,lines):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        while True:
                                iter +=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        print(''.join(data[-lines:]))
                                        break

file_read_from_tail('1910033.txt',2)

o/p:
I am from RIT
21 yrs. old
'''


#  5. Write a Python program to read a file line by line and store it into a list. 
'''
def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)

file_read('1910033.txt')

o/p:
['I am from RIT\n', '21 yrs. old']
'''
'''
#  6. Write a Python program to read a file line by line store it into a variable. 

def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('1910033.txt')

o/p:
['I am from RIT\n', '21 yrs. old']
'''

#  7. Write a python program to find the longest words. 
'''
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('1910033.txt'))

o/p:
['from', 'yrs.']
'''

#  8. Write a Python program to count the number of lines in a text file. 
'''
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("1910033.txt"))

o/p:
Number of lines in the file:  2
'''

#  9. Write a Python program to count the frequency of words in a file.  
'''
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("1910033.txt"))

o/p:
Number of words in the file : Counter({'I': 1, 'am': 1, 'from': 1, 'RIT': 1, '21': 1, 'yrs.': 1, 'old': 1})
'''

# 10. Write a Python program to get the file size of a plain file.
'''
def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("1910033.txt"))


o/p:
File size in bytes of a plain file:  26
'''
