"""
[기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기
https://codeup.kr/problem.php?id=6043

실수 2개(f1, f2)를 입력받아
f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

입력 예시
10.0 3.0

출력 예시
3.333
"""
a, b = input().split(" ")
a, b = float(a), float(b)
print(format((a / b), ".3f"))
