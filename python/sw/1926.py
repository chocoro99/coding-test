n = int(input())
count = 0

for i in range(1, n + 1):
    num = str(i)
    for z in range(len(num)):
        if "3" in num[z] or "6" in num[z] or "9" in num[z]:
            count += 1
    if count > 1:
        print("-" * count, end=" ")
    elif count == 1:
        print("-", end=" ")
    else:
        print(i, end=" ")
    count = 0
