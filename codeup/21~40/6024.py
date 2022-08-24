'''
[기초-입출력] 단어 2개 입력받아 이어 붙이기
https://codeup.kr/problem.php?id=6024

알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
순서대로 붙여 출력하는 프로그램을 작성해보자.

입력 예시
hello world

출력 예시
helloworld
'''
a,b = input().split(" ")
print(a,b, sep = "")