'''
[기초-3항연산] 정수 2개 입력받아 큰 값 출력하기
https://codeup.kr/problem.php?id=6063

입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.

입력 예시
123 456

출력 예시
456
'''
a,b = input().split(" ")
a,b = int(a), int(b)

print(a if(a>b) else b)