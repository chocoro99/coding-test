"""
예제 입력 1 
2
6 12 10
30 50 72
예제 출력 1 
402
1203"""
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split(" "))

    if n % h != 0 and n // h < 9:
        print(str(n % h) + "0" + str(n // h + 1))

    elif n % h != 0 and n // h >= 9:
        print(str(n % h) + str(n // h + 1))
    elif h == 1 and n // h < 9 and n != 1:
        print(str(h) + "0" + str(n // h + 1))
    elif n % h == 0 and n // h <= 9:
        print(str(h) + "0" + str(n // h))
    elif n % h == 0:
        print(str(h) + str(n // h))
