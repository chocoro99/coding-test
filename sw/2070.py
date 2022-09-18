t = int(input())
for i in range(1, t + 1):
    n = list(map(int, input().split(" ")))
    if n[0] > n[1]:
        print("#" + str(i), ">")
    elif n[0] < n[1]:
        print("#" + str(i), "<")
    elif n[0] == n[1]:
        print("#" + str(i), "=")
