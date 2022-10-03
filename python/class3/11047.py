n, k = map(int, input().split(" "))
m = []
count = 0

for i in range(n):
    m.append(int(input()))

for z in m[::-1]:
    if k // z >= 1:
        count += k // z
        k = k % z
print(count)
