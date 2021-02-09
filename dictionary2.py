# Looping through all key values pairs
student ={'name': 'Sumit','weight':'50','age':'21'}
print(student.items())
# dict_items([('name', 'Sumit'), ('weight', '50'), ('age', '21')])
for k, v in student.items():
        print(f'key={k},value={v}')
# key=name,value=Sumit
# key=weight,value=50
# key=age,value=21

# Loop through keys and values
countries ={
    'India':'New Delhi',
    'USA':'Washington DC',
    'UK': 'London'
}
for coun in countries.keys():
        print(coun)
# India
# USA
# UK

for coun in countries.keys():
        print(f'{coun} -> {countries[coun]}')
# India -> New Delhi
# USA -> Washington DC
# UK -> London

# Alphabetical sort
for coun in sorted (countries.keys()):
        print(f'{coun} -> {countries[coun]}')
# India -> New Delhi
# UK -> London        UK before USA
# USA -> Washington DC

# Looping thorugh keys
for cap in countries.values():
        print(cap)
# New Delhi
# Washington DC
# London

# you can access value with key but not vice-versa

print(countries.values())
# dict_values(['New Delhi', 'Washington DC', 'London'])
for cap in sorted (countries.values()):
        print(cap)
# London
# New Delhi
# Washington DC

# Nesting
# A list of dictionary
student1 ={'name': 'Sumit','weight':'60','age':'21'}
student2 ={'name': 'Rahul','weight':'55','age':'20'}
student3 ={'name': 'Neha','weight':'50','age':'19'}

students = [student1,student2,student3]
for stud in students:
        print(stud)
# {'name': 'Sumit', 'weight': '60', 'age': '21'}
# {'name': 'Rahul', 'weight': '55', 'age': '20'}
# {'name': 'Neha', 'weight': '50', 'age': '19'}

#Dictionary in List
output=[]
for value in range(1,6):
        output.append({'number':value, 'square':value*value})
print(output)
# [{'number': 1, 'square': 1}, {'number': 2, 'square': 4}, {'number': 3, 'square': 9}, {'number': 4, 'square': 16}, {'number': 5, 'square': 25}]

student ={'name': 'Sumit','weight':'60','hobbies':['trekking','music']}
for hobby in student['hobbies']:
        print(hobby)
# trekking
# music

# Dictionary in dictionary

students={
        'Sumit':{'weight':50,'height':160},
        'Rahul':
                {
                'weight':55,
                'height':150
                },
        'Neha':
                {
                'weight':45,
                'height':145
                }
}
for name in students.keys():
        print(f'name ={name}, weight={students[name]["weight"]}, height={students[name]["height"]}')
# name =Sumit, weight=50, height=160
# name =Rahul, weight=55, height=150
# name =Neha, weight=45, height=145