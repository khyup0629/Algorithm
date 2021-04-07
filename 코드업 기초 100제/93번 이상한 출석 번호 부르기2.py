# -*- coding: utf-8 -*-
n = int(input())
a = input().split(' ')

d=[]
for i in range(n):
    d.append(0)

for i in range(n):
    d[i] = a[n-i-1]
    print(d[i],end=' ')
