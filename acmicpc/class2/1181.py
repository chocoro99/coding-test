n = int(input())
list = []

for i in range(n):
    a = input()
    list.append(a)

list.sort()
list.sort(key=len)

print(list[0])
for i in range(1,n):
    if list[i] == list[i-1] or len(list[i])>50:
        continue
    print(list[i])