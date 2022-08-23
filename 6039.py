'''
[기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기
https://codeup.kr/problem.php?id=6039

실수 2개(f1, f2)를 입력받아
f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

입력 예시
4.0 2.0

출력 예시
16.0
'''
a,b = input().split(" ")
a,b = float(a), float(b)
print(a**b)