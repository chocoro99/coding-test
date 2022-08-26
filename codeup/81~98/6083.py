'''
[기초-종합] 빛 섞어 색 만들기
https://codeup.kr/problem.php?id=6083

빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.

빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.  

입력 예시
2 2 2

출력 예시
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
8
'''
a,b,c = input().split(" ")
a,b,c = int(a), int(b), int(c)
s = 0

for i in range(a) :
    for z in range(b) :
        for x in range(c) :
            print(i, z, x, sep = " ")
            s+=1
print(s)            