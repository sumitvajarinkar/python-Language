# Dictionary
#     - A collection of key/value pairs
#     - Each key is mapped to a value
#     - Use key to access the value maooed to it
#     - Keys -> Numbers, Strings
#     - Values -> Any data type like number, strings, lists, dictionaries,etc.

student ={'name': 'Sumit'} #key-value
print(type(student)) #<class 'dict'>

#Accessing key-value pair
student ={'name': 'Sumit', 'age':'21'}
print(student['name']) #Sumit
print(student['age']) #21

student ={'name': 'Sumit','weight':'50','age':'21'}
print(student) #{'name': 'Sumit', 'weight': '50', 'age': '21'}
print(student['name']) #Sumit
print(student['weight']) #50
print(student['age']) #21

#Add new key-value pair
student['height']=160
student['Gender']='male'
print(student) 
#{'name': 'Sumit', 'weight': '50', 'age': '21', 'height': 160, 'Gender': 'male'}

#Starting with an empty dictionary,
student={}
student['name']='Anil'
student['height']=160
student['weight']=50
print(student) #{'name': 'Anil', 'height': 160, 'weight': 50}


#modify value
student['height']=150
student['weight']=60
print(student) #{'name': 'Anil', 'height': 150, 'weight': 60}

#Dictionaries are mutable - add,delete and modify them
# key or values can be mutable or immutable depending on their type
# Strings -> immutable
# Numbers, lists -> mutable

student ={'name': 'Sumit','weight':'50','age':'21'}
# student['name'][0] ='s' 
print(student['name']) #error

#removing key value pairs
del student['name']
print(student)#{'weight': '50', 'age': '21'}

#mapping 
countries ={
    'India':'New Delhi',
    'USA':'Washington DC',
    'UK': 'London'
}
print(countries) #{'India': 'New Delhi', 'USA': 'Washington DC', 'UK': 'London'}

# using get() to access values in
#weight is absent
student ={'name': 'Sumit','age':'21'}
student.get('weight')
print(student.get('weight')) #None