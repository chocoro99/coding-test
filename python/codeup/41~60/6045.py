"""
[기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
https://codeup.kr/problem.php?id=6045

정수 3개를 입력받아 합과 평균을 출력해보자.

입력 예시
1 2 3

출력 예시
6 2.00
"""
a, b, c = input().split(" ")
a, b, c = int(a), int(b), int(c)
print((a + b + c), format(((a + b + c) / 3), ".2f"))
