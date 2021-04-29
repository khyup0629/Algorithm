# 시작점에서 시작해 시작점에서 끝날 경우를 고려해주고
# 나이트의 총 이동 경로 8방향을 고려하며 BFS로 해결하면 된다.
from collections import deque

t = int(input())


def bfs(s_x, s_y):
    # UL, UR, DL, DR, LU, LD, RU, RD
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]
    q = deque()
    q.append((s_x, s_y))
    visited[s_x][s_y] = True
    if s_x == e_x and s_y == e_y:
        return cost[s_x][s_y]
    while True:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    cost[nx][ny] = cost[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if nx == e_x and ny == e_y:
                    return cost[nx][ny]


for _ in range(t):
    n = int(input())
    # 2차원 방문 여부 리스트
    visited = [[False] * n for _ in range(n)]
    # 2차원 비용 리스트
    cost = [[0] * n for _ in range(n)]
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())
    print(bfs(s_x, s_y))

"""
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0
"""