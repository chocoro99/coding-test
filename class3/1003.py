"""zero = []
one = []


def fibonacci(n):
    if n == 0:
        zero.append(0)
        return 0
    elif n == 1:
        one.append(1)
        return 1
    else:
        return fibonacci(n - 1), fibonacci(n - 2)

t = int(input())
for i in range(t):
    a = int(input())
    fibonacci(a)
    print(len(zero), len(one))
"""
zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(n):
    length = len(zero)
    if n >= length:
        for i in range(length, n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[n], one[n])


t = int(input())

for _ in range(t):
    fibo(int(input()))
