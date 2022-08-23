'''
[기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기 2
https://codeup.kr/problem.php?id=6016

공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

입력 예시
a b

출력 예시
b a
'''
a,b = input().split()
a,b = int(a),int(b)
print(b,a)