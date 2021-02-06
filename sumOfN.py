arr=[]
n=int(input('Enter number of elements : '))
for i in range(0,n):
    ele=int(input('Enter elements : '))
    arr.append(ele)
if n>0:
    sum=0
    for i in range(0,n):
        sum+=arr[i]
    print(f'Sum is :{sum}')
else:
    print('List is empty')



