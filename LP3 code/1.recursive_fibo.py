def fibonacci(n):
    if n<=1:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n = int(input('Enter the no. of terms: '))
for i in range(n):
    print(fibonacci(i), end = ' ')
