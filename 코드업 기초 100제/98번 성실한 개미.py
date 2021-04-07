# -*- coding: utf-8 -*-
d = [[0 for j in range(11)] for i in range(11)]

for i in range(1, 11):
    a = input().split(' ')
    for j in range(10):
        d[i][j + 1] = int(a[j])

x = 2
y = 2
d[x][y] = 9
while d[x][y] != 2:
    if d[x][y + 1] == 1:
        x += 1
        if d[x][y] == 1:
            x -= 1
            d[x][y] = 2
            continue
        elif d[x][y] == 2:
            continue
        else:
            d[x][y] = 9
    elif d[x][y + 1] == 0:
        y += 1
        d[x][y] = 9
    elif d[x][y + 1] == 2:
        y += 1
        continue
d[x][y] = 9

for i in range(1, 11):
    for j in range(1, 11):
        print(d[i][j], end=' ')
    print()
