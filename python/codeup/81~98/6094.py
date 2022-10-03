'''
[기초-리스트] 이상한 출석 번호 부르기3
https://codeup.kr/problem.php?id=6094

정보 선생님은 오늘도 이상한 출석을 부른다.

영일이는 오늘도 다른 생각을 해보았다.
출석 번호를 다 부르지는 않은 것 같은데... 가장 빠른 번호가 뭐였지?

출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

입력 예시
10
10 4 2 3 6 6 7 9 8 5

출력 예시
2
'''
a = int(input())
b = input().split(" ")
n = 100

for i in range(a):
    b[i] = int(b[i])

for z in range(a):
    if n > b[z]:
        n = b[z]
print(n)        