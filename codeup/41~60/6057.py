'''
[기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
https://codeup.kr/problem.php?id=6057

2개의 정수값이 입력될 때,
그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

입력 예시
0 0

출력 예시
True
'''
a,b = input().split(" ")
a,b = int(a), int(b)

if bool(a) == bool(b) :
  print("True")
else :
  print("False")