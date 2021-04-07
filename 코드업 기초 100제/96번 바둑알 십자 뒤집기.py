# -*- coding: utf-8 -*-
d = [[0 for j in range(20)] for i in range(20)]

for i in range(1,20):
    a = input().split(' ')
    for j in range(19):
        d[i][j+1] = int(a[j])

n = int(input())
for i in range(n):
    x,y = map(int,input().split(' '))
    for j in range(1,20):
        if j == y:
            continue
        else:
            if d[x][j] == 0:
                d[x][j] = 1
            else:
                d[x][j] = 0
    for j in range(1,20):
        if j == x:
            continue
        else:
            if d[j][y] == 0:
                d[j][y] = 1
            else:
                d[j][y] = 0

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=' ')
    print()
