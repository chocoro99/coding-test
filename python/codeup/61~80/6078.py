"""
[기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
https://codeup.kr/problem.php?id=6078

영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.

입력 예시
x
b
k
d
l
q
g
a
c

출력 예시
x
b
k
d
l
q
"""
while True:
    a = input()
    if a == "q":
        print(a)
        break
    else:
        print(a)
