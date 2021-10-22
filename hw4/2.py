def fib(n):
    c = 1
    j = 1
    i = 1
    while (i < n):
        c, j, i = c+j, c, i+1
    return c
for i in range(10):
    print(fib(i))

