n = int(input())
num_list = list(map(int, input().split(" ")))
max_num = num_list[0]
min_num = num_list[0]

for i in range(n):
    max_num = max(max_num, num_list[i])
    min_num = min(min_num, num_list[i])
print(min_num, max_num, sep=" ")