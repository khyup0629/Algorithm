# -*- coding: utf-8 -*-
a,b = map(int,input().split(' '))
# a : 현재 온도, b : 목표 온도

n = 0
while a != b:
    if (b - a >= 8):
        a += 10
    elif (b - a >= 3):
        a += 5
    elif (b - a >= 1):
        a += 1
    elif (a - b >= 8):
        a -= 10
    elif (a - b >= 3):
        a -= 5
    else:
        a -= 1
    n += 1

print(n)