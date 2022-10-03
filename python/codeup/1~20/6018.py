'''
[기초-입출력] 문장 1개 입력받아 3번 출력하기
https://codeup.kr/problem.php?id=6018

24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

입력 예시
3:16

출력 예시
3:16
'''
a,b = input().split(':')
a,b = int(a), int(b)
print(a,b,sep=(':'))