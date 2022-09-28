t = int(input())
for i in range(1, t + 1):
    n = int(input())
    l = []
    print("#" + str(i))
    for z in range(1, n + 1):
        a = []
        for x in range(1, z + 1):
            if x == 1 or x == z:
                a.append(1)
            else:
                a.append(l[z - 2][x - 1] + l[z - 2][x - 2])
            print(a[x - 1], end=" ")
        print()
        l.append(a)
