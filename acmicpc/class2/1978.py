n = int(input())
n_list = list(map(int, input().split(" ")))
count = n

for i in n_list:
    if i !=1:
        for z in range(2,i):            
            if i%z ==0 :
                count-=1
                break
    if i == 1:
        count-=1
print(count)