n = int(input())
answer = 0
a = 0
p = list(map(int, input().split(" ")))
p.sort()

for i in range(0, n):
    a += p[i]
    answer += a

print(answer)
