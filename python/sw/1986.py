t = int(input())

for i in range(1, t + 1):
    n = int(input())
    if n % 2 == 0:
        print("#" + str(i), -(n // 2))
    else:
        print("#" + str(i), (n + 1) // 2)
