t = int(input())
for i in range(1, t + 1):
    n = list(map(int, input().split(" ")))
    for z in n:
        if n[0] < z:
            n[0] = z
    print("#" + str(i), n[0])
