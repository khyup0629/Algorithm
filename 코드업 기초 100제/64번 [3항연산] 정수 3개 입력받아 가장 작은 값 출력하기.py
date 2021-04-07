# -*- coding: utf-8 -*-
n = input().split(' ')
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = (a if (a<b) else b) if ((a if (a<b) else b)<c) else c
print(d)
