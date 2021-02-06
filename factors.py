n=int(input('Enter number of elements : '))
print(f'Factors of {n} are : ')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')