def fibonacci(n):
    fib = [1,1]

    for i in range(1,n-1):
        fib.append(fib[i-1] + fib[i])
    
    return fib[-2], fib[-1]

N = int(input())
inputs = [int(input()) for _ in range(N)]

for i in inputs:
    if i == 0:
        print(1, 0)
    elif i == 1:
        print(0, 1)
    else:
        zero, one = fibonacci(i)
        print(zero, one)