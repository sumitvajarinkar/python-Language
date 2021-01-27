names=['Sumit', 'saket', 'Avni']
print(names[0])
print(names[1])
print(names[2])
print(names[0],names[1],names[2])

# we need for loop to access number of elements
# for loop
# name is variable, so it points the element in the names (meaningful)
# for plural names we use singular as name for variable
for name in names:
    print(name) 
#will print loop like : 
# Sumit
# saket
# Avni
# 2 lines in loop is belongs to loop
for name in names:
    print(f'Everybody knows {name} is a champian')
    print('champion..champion..champion..')
# Everybody knows Sumit is a champian
# champion..champion..champion..
# Everybody knows saket is a champian
# champion..champion..champion..
# Everybody knows Avni is a champian
# champion..champion..champion..

#So, why identation is require in Python(Identation is MUST in PYTHON)
# for this 1st line will print 3 times after 2nd line prints 1 time

for name in names:
    print(f'Everybody knows {name} is a champian')
    print('champion..champion..champion..')
# Everybody knows Sumit is a champian
# Everybody knows saket is a champian
# Everybody knows Avni is a champian
# champion..champion..champion..
    
    # logical error but not identation errors(use tabs/spaces must 1)
    # don't combine tabs and spaces it may give error and it will take long time to debug
    # depends on Editor, I use VS Code
