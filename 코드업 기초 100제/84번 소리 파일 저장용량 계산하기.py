# -*- coding: utf-8 -*-
h, b, c, s = map(int,input().split(' '))
data = h * b * c * s / 8 / 1024 / 1024
print(format(data,'.1f'),'MB')
