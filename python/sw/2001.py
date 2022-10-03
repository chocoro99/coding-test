t = int(input())

for i in range(1, t + 1):
    max = 0
    s = []
    n, m = map(int, input().split(" "))
    for z in range(n):
        s.append(list(map(int, input().split(" "))))

    for x in range(n - m + 1):
        for r in range(n - m + 1):
            temp = 0
            for j in range(m):
                for h in range(m):
                    temp += s[x + j][r + h]
            if temp > max:
                max = temp
    print("#" + str(i), max)
