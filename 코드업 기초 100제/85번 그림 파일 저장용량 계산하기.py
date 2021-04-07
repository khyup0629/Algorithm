# -*- coding: utf-8 -*-
w, h, b = map(int,input().split(' '))
data = w * h * b / 8 / 1024 / 1024
print(format(data,'.2f'),'MB')
