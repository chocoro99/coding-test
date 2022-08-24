'''
[기초-비교연산] 정수 2개 입력받아 비교하기1
https://codeup.kr/problem.php?id=6048

두 정수(a, b)를 입력받아
a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

입력 예시
1 9

출력 예시
True
'''
a,b = input().split(" ")
a,b = int(a), int(b)
if a < b :
  print("True")
elif a >= b :
  print("False")