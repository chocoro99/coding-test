"""
예제 입력 1 
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
예제 출력 1 
2
2
0
2
1
-1
0
1
-1
0
3
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다."""
import sys

n = int(sys.stdin.readline())
n_list = []

for i in range(n):
    a = sys.stdin.readline().strip().split(" ")
    if "push" in a:
        n_list.append(a[1])
    elif "pop" in a:
        print(n_list.pop() if len(n_list) != 0 else "-1")
    elif "size" in a:
        print(len(n_list))
    elif "empty" in a:
        print("1" if len(n_list) == 0 else "0")
    elif "top" in a:
        print(n_list[-1] if len(n_list) != 0 else "-1")
