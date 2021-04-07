# -*- coding: utf-8 -*-
n = int(input())
a = input().split(' ')

for i in range(n):
    a[i] = int(a[i])

s = a[0]
for i in range(1, n):
    if s >= a[i]:
        s = a[i]
print(s)
