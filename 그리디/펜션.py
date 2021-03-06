# -*- coding: utf-8 -*-
n, m = map(int, input().split(' '))
d = [0 for i in range(n)]
result = -1
for i in range(n):
    x = input()
    d[i] = list(x)

s, t = map(int, input().split(' '))
i = s - 1

while i != (t - 1):
    b = 0
    best = 0
    for j in range(m):
        if d[i][j] == 'X':
            continue
        elif d[i][j] == 'O':
            a = 1
            for k in range(i + 1, t - 1):
                if d[k][j] == 'O':
                    a += 1
                else:
                    break
            if a > best:
                best = a
                b = i + a
    if best == 0:
        result = -1
        break
    else:
        i = b
        result += 1

print(result)

'''
입력 예시

10 7
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
XXXXXXX
2 9

10 7
XXXXXXX
XOXXOXX
XXOXOXX
XXXXXXX
XXOXXOX
XXXXOXO
XXXXOXO
XXXXXXO
XXXXXOX
XXXXXXX
4 5

10 7
XXXXXXX
XOXXXXO
XOXXXXO
XXXXXXX
OXXOXOX
XOXOXOX
OXXOXOX
OXXXXOX
XXXXXXX
XXXXXXX
2 9
'''