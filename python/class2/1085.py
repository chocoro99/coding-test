x, y, w, h = map(int, input().split(" "))
p_x = 0
p_y = 0

if w - x >= x:
    p_x = x
else:
    p_x = w - x

if h - y >= y:
    p_y = y
else:
    p_y = h - y

if p_x >= p_y:
    print(p_y)
else:
    print(p_x)
