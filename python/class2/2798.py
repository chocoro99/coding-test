n, m = map(int, input().split(" "))
card = list(map(int, input().split(" ")))
answer = 0

for i in range(n):
    for z in range(n):
        if z == i:
            continue
        for x in range(n):
            if x == i or x == z:
                continue
            jack = card[i] + card[z] + card[x]
            if jack <= m and jack > answer:
                answer = jack
print(answer)
