# -*- coding: utf-8 -*-
n = int(input())
a, b = map(int, input().split(' '))
c = int(input())

d = []
for i in range(n):
    d.append(0)

for i in range(n):
    s = int(input())
    d[i] = s

d.sort()
d.reverse()
d.insert(0, 0)
price = 0
best = c // a
for i in range(n + 1):
    cal = c
    price = a + (i * b)
    for j in range(i + 1):
        cal += d[j]
    calperprice = cal // price
    if best < calperprice:
        best = calperprice
print(best)
