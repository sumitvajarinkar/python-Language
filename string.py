
# single quote vs double quotes
#be consistent
#use only 1 in each program



message='my name is sumit'
print(message)
message="my name is sumit"
print(message)
message="my name is 'sumit'"
print(message)
message='my name is "sumit"'
print(message)

# upper and lower
# original data doesn't change
message='My NaMe iS"suMit"'
print(message.upper())
# print(message) will print original msg

message='My NaMe iS "SUMIT"'
print(message.lower())

# for permanent change
message=message.lower() #override it
print(message)

# Title function - converts 1st char of each word into upper case 
name="sUmit vAjarinkar"
print(name.title())
# o/p Sumit Vajarinkar

# len function
x="abc "
print(len(x))

# strip()-both lstrip() rstrip() l,r are left right
# remove extra whitespaces of string

# right
str1='python  '
print(len(str1))
str1.rstrip()
print(str1)
str1=str1.rstrip()
print(len(str1))
# left
str2=' python'
print(len(str2))
str2.lstrip()
print(str2)
str2=str2.lstrip()
print(str2)
print(len(str2))

# combine two string starting with f(format) put curly braces
first_name='sumit'
last_name='vajarinkar'
full_name=f'my name is {first_name} {last_name}'
print(full_name)
print(f'My full name is {first_name.title()} {last_name.title()}')

# Concatenate

full_name=first_name+" "+last_name
print(full_name)

# Adding whitespace to strings with tabs or Newlines
name='\tSumit'
print(name)                   
name='\tSumit\n\tVajarinkar'
print(name)                   