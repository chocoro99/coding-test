'''
[기초-논리연산] 하나라도 참이면 참 출력하기
https://codeup.kr/problem.php?id=6055

2개의 정수값이 입력될 때,
그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

입력 예시
1 1

출력 예시
True
'''
a,b = input().split(" ")
a,b = int(a), int(b)

if bool(a) == True or bool(b) == True :
  print("True")
else :
  print("False")