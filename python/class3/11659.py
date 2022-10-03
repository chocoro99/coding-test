import sys

n, m = map(int, sys.stdin.readline().strip().split(" "))
a = list(map(int, sys.stdin.readline().strip().split(" ")))
b = [0]
temp = 0
for h in a:
    temp += h
    b.append(temp)

for z in range(m):
    i, j = map(int, sys.stdin.readline().strip().split(" "))
    print(b[j] - b[i - 1])
