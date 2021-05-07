# DFS로 해결하였다.

import sys
sys.setrecursionlimit(10**6)

n = int(input())

frame = []
for _ in range(n):
    array = list(map(int, input()))
    frame.append(array)

answer = ''


def dfs(n, point):
    global answer
    # 왼위, 오위, 왼아래, 오아래 순서로 point에 저장된 시작점에서 탐색 시작
    for x, y in point:
        changed = False  # 현재 칸의 모든 원소가 통일되었는지
        # 현재 4등분 된 칸 중의 하나에 속해 있는 모든 원소 탐색
        for i in range(x, x+n):
            for j in range(y, y+n):
                if frame[i][j] != frame[x][y]:  # 하나라도 다른 원소가 있다면
                    answer += '('
                    interval = n // 2
                    # 왼위, 오위, 왼아래, 오아래
                    # 현재 칸을 4등분 했을 때 탐색의 시작점 4곳 기록
                    point = [(x, y), (x, y+interval), (x+interval, y), (x+interval, y+interval)]
                    dfs(interval, point)  # 현재 칸을 더 작게 4등분
                    changed = True  # 원소가 하나라도 다르다.
                    break
            if changed:  # 하나라도 다른 원소가 있다면 더이상
                break  # 다른 원소가 존재하는지 반복할 필요 없다.
        # 현재 칸의 탐색이 끝나고 모든 칸이 통일되었을 경우 answer에 기록
        if not changed:
            answer += str(frame[x][y])
    # 전체 칸의 탐색이 끝나면 닫아준다.
    answer += ')'
    return


for i in range(n):
    changed = False
    for j in range(n):
        if frame[i][j] != frame[0][0]:
            answer += '('
            # 왼위, 오위, 왼아래, 오아래
            point = [(0, 0), (0, n//2), (n//2, 0), (n//2, n//2)]
            dfs(n//2, point)  # 전체 칸 4등분부터 시작.
            changed = True
            break
    if changed:  # 현재 탐색하는 구간의 원소가 다르다면 반복 멈추기.
        break
if not changed:  # 모든 구간의 원소가 같다면,
    print(frame[0][0])
else:
    print(answer)

# 문제 : https://www.acmicpc.net/problem/1992
"""
예제 입력 2
4
1111
1111
1111
1111
예제 출력 2
1
"""
