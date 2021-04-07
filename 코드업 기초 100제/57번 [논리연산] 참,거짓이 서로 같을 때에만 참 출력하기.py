# -*- coding: utf-8 -*-
n = input().split(' ')
a = bool(int(n[0]))
b = bool(int(n[1]))
print((a or not b) and (not a or b))
