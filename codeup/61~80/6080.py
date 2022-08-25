'''
[기초-종합] 주사위 2개 던지기
https://codeup.kr/problem.php?id=6080

1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.

입력 예시
2 3

출력 예시
1 1
1 2
1 3
2 1
2 2
2 3
'''
a,b = input().split(" ")
a,b = int(a), int(b)

for i in range(1, a+1) :
    for z in range(1, b+1) :
        print(i, z)