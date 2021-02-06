arr=[]
n=int(input('Enter number of elements : '))
for i in range(0,n):
    ele=int(input('Enter elements : '))
    arr.append(ele)
if n>0:
    larger=arr[0]
    for i in range(0,n):
        if arr[i]>larger:
            larger=arr[i]
    print(f'Large element is :{larger}')
else:
    print('List is empty')



