# -*- coding: utf-8 -*-
h,w = map(int,input().split(' '))

a = [[0 for j in range(w+1)] for i in range(h+1)]

n = int(input())
for i in range(n):
    l,d,x,y = map(int,input().split(' '))
    # l : 막대의 길이, d : 방향(가로 : 0, 세로 : 1), x,y:막대의 시작점
    if d == 0:
        for j in range(y,y+l):
            a[x][j] = 1
    else:
        for j in range(x,x+l):
            a[j][y] = 1

for i in range(1,h+1):
    for j in range(1,w+1):
        print(a[i][j],end=' ')
    print()
