# -*- coding: utf-8 -*-
n = input().split(' ')
a = bool(int(n[0]))
b = bool(int(n[1]))
print((a and not b) or (not a and b))
