# -*- coding: utf-8 -*-
a,r,n = map(int, input().split(' '))
for i in range(1,n):
    a *= r
print(a)
