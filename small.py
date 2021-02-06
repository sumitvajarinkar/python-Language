arr=[]

n=int(input('Enter number of elements : '))
for i in range(0,n):
    ele=int(input('Enter elements : '))
    arr.append(ele)
if n>0:
    smaller=arr[0]
    for i in range(0,n):
        if arr[i]<smaller:
            smaller=arr[i]
    print(f'Small element is :{smaller}')
else:
    print('List is empty')
