# Check if given number is odd or even
num=int(input())
if num & 1 == 0: # num % 2==0
    print('Even')
else:
    print('Odd')