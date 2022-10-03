t = int(input())

for i in range(t):
    a = [1, 1, 1]
    n = int(input())

    if n == 1 or n == 2 or n == 3:
        print(a[n - 1])
    for z in range(3, n):
        a.append(a[z - 2] + a[-3])
        if z == n - 1:
            print(a[z])
