'''
[기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
https://codeup.kr/problem.php?id=6065

3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

입력 예시
1 2 4

출력 예시
2
4
'''
a,b,c = input().split(" ")
a,b,c = int(a), int(b), int(c)

if a%2 == 0:
    print(a)
if b%2 == 0:
    print(b)
if c%2 == 0:
    print(c)    