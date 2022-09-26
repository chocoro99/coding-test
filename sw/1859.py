t = int(input())
price = 0
profit = 0
for i in range(1, t + 1):
    n = int(input())
    price_list = list(map(int, input().split(" ")))
    price_list = price_list[::-1]
    profit = 0
    price = 0
    for z in price_list:
        if z > price:
            price = z
        else:
            profit = profit + price - z
    print("#" + str(i), profit)
