'''
[기초-논리연산] 참 거짓 바꾸기
https://codeup.kr/problem.php?id=6053

정수값이 입력될 때,
그 불 값을 반대로 출력하는 프로그램을 작성해보자.

입력 예시
1

출력 예시
False
'''
a = int(input())
print(not bool(a))