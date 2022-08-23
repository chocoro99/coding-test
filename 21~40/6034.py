'''
[기초-산술연산] 정수 2개 입력받아 차 계산하기
https://codeup.kr/problem.php?id=6034

정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

입력 예시
123 -123

출력 예시
246
'''
a,b = input().split(" ")
a,b = int(a), int(b)
print(a-b)