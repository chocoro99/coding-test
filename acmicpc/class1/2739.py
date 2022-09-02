t = int(input())

for i in range(t):
    r = input().split(" ")
    s = ""
    for z in r[1]:
        s += z*int(r[0])
    print(s)