a = int(input())

for i in range(a):
    l = input()
    sum_num = 0
    count = 1
    for z in l:        
        if z == 'O':
            sum_num += count   
            count +=1            
        elif z == 'X':
            count = 1                      
    print(sum_num)