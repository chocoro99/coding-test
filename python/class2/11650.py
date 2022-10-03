import sys

n = int(sys.stdin.readline())
pos_list = []

for i in range(n):
    pos_list.append(list(map(int, sys.stdin.readline().split(" "))))
pos_list.sort()
for i in pos_list:
    print(" ".join(map(str, (i))))
