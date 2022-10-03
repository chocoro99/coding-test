from collections import deque

n = int(input())
n_list = deque()

for i in range(1,n+1):
    n_list.append(i)

while len(n_list) > 1:    
    n_list.popleft()        
    n_list.append(n_list.popleft())             
print(n_list[0])