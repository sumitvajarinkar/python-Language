# Default values
# One can define default values for each function parameter
# if an argument foe a parameter is not passed, default value is used

def main(name,country='India'):
    print(f'Hello{name}, {country}')
main('') 
# Hello, India

# Default value follows default value
# Error, after default values there must be default value not non-default
# def main(name='',country):
#     print(f'Hello{name}, {country}')
# main('India') 

# Return values
def multiply(n1,n2):
    return n1*n2
result = multiply(2,3)
print(result) #6


def multiply(n1,n2):
    return f'{n1}*{n2}={n1*n2}'
result = multiply(2,3)
print(result) #2*3=6


# while in function
# press ctrl + c to interrupt infinite loop

# def format(first_name,last_name):
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()                #return with 1st letter uppercase
# i=0
# while i<2 :
#     first_name=input('Enter first name : ')
#     last_name=input('Enter last name : ')
#     formatted=format(first_name, last_name)
#     print(f'Hello {formatted}')
#     i+=1

# Enter first name : sumit
# Enter last name : vajarinkar
# Hello Sumit Vajarinkar
# Enter first name : saket
# Enter last name : chavan
# Hello Saket Chavan
# Enter first name :


# passing list to function

def main(names):
    for name in names:
        print(f'Hello {name}')

main(['Sumit','Rahul','Neha'])
# Hello Sumit
# Hello Rahul
# Hello Neha

# modifying a list in function

def main(names):
    names.sort()
    for name in names:
        print(f'Hello {name}')
names =['Sumit','Rahul','Neha'] 
main(names)

# Hello Neha
# Hello Rahul
# Hello Sumit

print(names)
# ['Neha', 'Rahul', 'Sumit']

# dictionary

def main(dict):
    dict['name']='Rahul'
    print(dict)
d={'name':'Neha'}
main(d)
print(d)
# {'name': 'Rahul'}
# {'name': 'Rahul'}

# by using copy 
def main(dict):
    dict['name']='Rahul'
    print(dict)
d={'name':'Neha'}
main(d.copy())
print(d)
# {'name': 'Rahul'}
# {'name': 'Neha'}

