'''
[기초-값변환] 정수 2개 입력받아 합 계산하기
https://codeup.kr/problem.php?id=6025

정수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.

입력 예시
123 -123

출력 예시
0
'''
a,b = input().split(" ")
a,b = int(a), int(b)
print(a+b)