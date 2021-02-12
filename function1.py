# def is keyword, syntax of writing function

# defination of function
def main():
    print('hello !') #hello !
main()          #call to function

# function can call many times when we use so its reduce thelength of code and increase reuseability too

# defination
def greater(x,y):
    if x>y:
        print(f'{x} is Greater than {y}')
    else:
        print(f'{y} is Greater than {x}')
#function call 
greater(5,9)
greater(1132,243)

# 9 is Greater than 5
# 1132 is Greater than 243


# user defined vs built-in functions
# built-in : print(), len(), sort() 

# calling function have arguments 
# called function have parameters

# passing parametes
def main(name):
    print(f'Hello {name} !')
main('Sumit')
main('Rahul')
main('Neha')
# Hello Sumit !
# Hello Rahul !
# Hello Neha !

# multiple arguments, 
# positional arguments : 3 arguments require 3 parameters
def main(name,country):
    print(f'Hello {name}, {country}')

main('Sumit', 'India') 
#Hello Sumit, India


# keyword arguments
def main(name,country):
    print(f'Hello {name}, {country}')
main(name='Sumit', country='India') 

# Hello Sumit, India

# using keyword and positional arguments get error
# def main(name,country):
#     print(f'Hello {name}, {country}')
# main(name='Sumit','India')
# SyntaxError: positional arguement follows keyword argument  

# Interchangable keyword arguement will work fine
def main(name,country):
    print(f'Hello {name}, {country}')
main(country='India',name='Sumit') 
# Hello Sumit, India

# Changable the positional arguement will work fine
# but Changable
def main(name,country):
    print(f'Hello {name}, {country}')
main('India','Sumit') 
# Hello Sumit, India
