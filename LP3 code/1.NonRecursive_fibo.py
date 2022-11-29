n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n = int(input('Enter no. of terms: '))
print(n1,n2, end = ' ')
while(n-2):
    c = n1+n2
    n1 = n2
    n2 = c
    print(c, end = ' ')
    n = n-1
