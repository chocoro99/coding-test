'''
[기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
https://codeup.kr/problem.php?id=6066

3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

입력 예시
1 2 8

출력 예시
odd
even
even
'''
a,b,c = input().split(" ")
a,b,c = int(a), int(b), int(c)

print("odd" if(a%2==0) else "even")
print("odd" if(b%2==0) else "even")
print("odd" if(c%2==0) else "even") 