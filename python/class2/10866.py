"""
예제 입력 1 
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
예제 출력 1 
2
1
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
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다."""
import sys

n = int(sys.stdin.readline())
n_list = []

for i in range(n):
    a = sys.stdin.readline().strip().split(" ")
    if a[0] == "push_front":
        n_list.insert(0, a[1])
    elif a[0] == "push_back":
        n_list.append(a[1])
    elif a[0] == "pop_front":
        print(n_list.pop(0) if len(n_list) != 0 else "-1")
    elif a[0] == "pop_back":
        print(n_list.pop() if len(n_list) != 0 else "-1")
    elif a[0] == "size":
        print(len(n_list))
    elif a[0] == "empty":
        print("1" if len(n_list) == 0 else "0")
    elif a[0] == "front":
        print(n_list[0] if len(n_list) != 0 else "-1")
    elif a[0] == "back":
        print(n_list[-1] if len(n_list) != 0 else "-1")
