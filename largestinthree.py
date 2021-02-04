#Find the largest number in given three
n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2 and n1>n3:
        print(f'{n1} is largest')
elif n2>n3:
    print(f'{n2} is largest')
else:
    print(f'{n3} is largest')
        