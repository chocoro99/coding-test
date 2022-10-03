'''
[기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기
https://codeup.kr/problem.php?id=6038

정수 2개(a, b)를 입력받아
a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

입력 예시
2 10

출력 예시
1024
'''
a,b = input().split(" ")
a,b = int(a), int(b)
print(a**b)