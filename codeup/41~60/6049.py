'''
[기초-비교연산] 정수 2개 입력받아 비교하기2
https://codeup.kr/problem.php?id=6049

두 정수(a, b)를 입력받아
a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

입력 예시
0 0

출력 예시
True
'''
a,b = input().split(" ")
a,b = int(a), int(b)

if a == b :
  print("True")
elif a != b :
  print("False")