'''
[기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기
https://codeup.kr/problem.php?id=6064

입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.

입력 예시
3 -1 5

출력 예시
-1
'''
a,b,c = input().split(" ")
a,b,c = int(a), int(b), int(c)

print((a if(a<b) else b) if((a if(a<b) else b) < c) else c)