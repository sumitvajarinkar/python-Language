# Python classes and objects

#1.	Write a Python program to create an instance of a specified class and display the namespace of the said instance.(Class: student, Attributes: id, name, class name)

'''
class Student: 
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name
n=int(input('Enter PRN \n'))   
nm=(input('Enter name \n'))   
branch=(input('Enter branch \n'))   
student = Student(n, nm, branch)
print(student.__dict__)
o/p:
{'student_id': '1910033', 'student_name': 'Sumit Vajarinkar', 'class_name': 'CSIT'}
'''

#2.	Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given format.

'''
class Student:
    school = 'RIT'
    address = 'Sakharale' 
student1 = Student()
student2 = Student() 
student1.student_id = "1910033"
student1.student_name = "Sumit Vajarinkar"
student2.student_id = "1910021"
student2.marks_language = 85
student2.marks_science = 92
student2.marks_math = 92 
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
    
o/p:

student_id -> 1910033
student_name -> Sumit Vajarinkarz


student_id -> 1910021
marks_language -> 85
marks_science -> 92
marks_math -> 92
'''

# 3.	Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

'''
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(4, 3)
print(newRectangle.rectangle_area())

o/p:
12
'''

# 4.	Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.
'''
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()

o/p:
sumit
SUMIT
'''
# 5.	Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
'''
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(4)
print(f'Area is {NewCircle.area()}')
print(f'Perimeter is {NewCircle.perimeter()}')

o.p:
Area is 50.24
Perimeter is 25.12
'''


# 6.Implement the Customer class based on the identified class structure and details given below:
# a. Consider all instance variables and methods to be public
# b. Assume that bill_amount is initialized with total bill amount of the customer
# c. Customer is eligible for 5% discount on the bill amount
# d. purchases(): Compute discounted bill amount and pay bill
# e. pays_bill(amount): Display, <customer_name> pays bill amount of Rs. <amount> Represent few customers, invoke purchases() method and display the details.


'''
class Customer():

    def __init__(self,name,amount):
        self.name=name
        self.bill_amount=amount
    def purchases(self):
        self.discount=self.bill_amount*0.05
        self.bill_amount-= self.bill_amount*0.05

    def pays_bill(self,amount):
        self.purchases()
        print(f"{self.name} Paid {self.bill_amount} and {self.discount}rs discount is applied")

x=Customer("Rahul",500)

x.pays_bill(1000)
Output--
Rahul Paid 475.0 and 25.0rs discount is applied

'''