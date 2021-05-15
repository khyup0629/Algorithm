# 1. 처음 4등분에서 어디에 속해 있는지
# 2. 속한 부분으로 들어가서 다시 4등분
# 3. 1과 2를 반복.

import sys
sys.setrecursionlimit(10**5)

n, r, c = map(int, input().split())


def dfs(l, point, element):
    global cnt, result
    x, y = point[0], point[1]
    # 첫 번째 사각형
    if x <= r < x+l and y <= c < y+l:
        cnt += (element // 4) * 0
        if l != 1:
            standard = l // 2
            point = (x, y)
            element_m = element // 4
            dfs(standard, point, element_m)
        else:
            result = cnt
            return
    # 두 번째 사각형
    elif x <= r < x+l and y + l <= c < y + 2 * l:
        cnt += (element // 4) * 1
        if l != 1:
            standard = l // 2
            point = (x, y+l)
            element_m = element // 4
            dfs(standard, point, element_m)
        else:
            result = cnt
            return
    # 세 번째 사각형
    elif x + l <= r < x + 2 * l and y <= c < y+l:
        cnt += (element // 4) * 2
        if l != 1:
            standard = l // 2
            point = (x+l, y)
            element_m = element // 4
            dfs(standard, point, element_m)
        else:
            result = cnt
            return
    # 네 번째 사각형
    else:
        cnt += (element // 4) * 3
        if l != 1:
            standard = l // 2
            point = (x+l, y+l)
            element_m = element // 4
            dfs(standard, point, element_m)
        else:
            result = cnt
            return


l = 2 ** n
standard = l // 2
element = (2 ** n) * (2 ** n)
point = (0, 0)
cnt, result = 0, 0

dfs(standard, point, element)

print(result)

# 문제 : https://www.acmicpc.net/problem/1074
