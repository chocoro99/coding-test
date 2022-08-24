'''
[기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기
https://codeup.kr/problem.php?id=6040

정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

입력 예시
10 3

출력 예시
3
'''
a,b = input().split(" ")
a,b = int(a), int(b)
print(a//b)