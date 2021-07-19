# 전형적인 분할 정복 문제입니다.

import sys
sys.setrecursionlimit(10**5)
n = int(input())
graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)


def divide_conquer(point, n):
    global cnt_white, cnt_blue
    for x, y in point:
        init = graph[x][y]  # 시작점의 색종이 색, 색을 비교하기 위한 기준
        changed = False  # 현재 분할된 색종이의 색이 모두 같은지
        for nx in range(x, x+n):
            for ny in range(y, y+n):
                if init != graph[nx][ny]:  # 처음 색과 다르다면
                    point = [(x, y), (x+n//2, y), (x, y+n//2), (x+n//2, y+n//2)]
                    divide_conquer(point, n//2)
                    changed = True  # 색종이의 색이 모두 같지 않으면 변경
                    break  # 반복 종료
            if changed:  # 색이 모두 같지 않으면 반복 종료
                break
        if not changed:
            if init == 0:  # 흰 종이 개수 세기
                cnt_white += 1
            else:  # 파란 종이 개수 세기
                cnt_blue += 1


cnt_white, cnt_blue = 0, 0
point = [(0, 0)]
divide_conquer(point, n)
print(cnt_white)
print(cnt_blue)

# 문제 : https://www.acmicpc.net/problem/2630
