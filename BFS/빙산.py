# 문제 풀이 아이디어 : BFS
# 1. BFS 로 탐색하면서 graph 의 원소를 갱신시키면 다음 노드를 탐색할 때 제약이 발생한다.
# 2. cost 를 두고 0과 접한 개수를 여기다 저장한 후 1년이 지날 때 한 번에 graph 를 갱신시켜준다.
# 3. 모두 연결되어 있다면 BFS 를 한 번 돌릴 때 모든 원소가 탐색이 될 것이다.
# BFS 를 두 번 탐색하게 되면 빙산이 분리된 것이므로 반복을 멈추고 그 전까지 반복 횟수를 출력한다.
# 4. BFS 탐색 후 cost 값을 graph 에 반영하면서 graph 의 원소 중에 0 이상인 것의 개수를 체크한다.
# 그 개수가 만약 0이라면 빙산이 계속 한 덩이인채로 모두 녹았다는 것으로 0을 출력한다.
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    lst = list(map(int, input().split()))
    graph.append(lst)


def bfs(s_x, s_y):
    q = deque()
    q.append((s_x, s_y))
    visited[s_x][s_y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        cnt_0 = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 인접한 4방향 탐색
                if graph[nx][ny] > 0 and not visited[nx][ny]:  # 아직 미방문 상태이면서 0보다 큰 값이면,
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] <= 0:  # 0보다 작거나 같은 값이면,
                    cnt_0 += 1  # 인접한 0의 개수를 센다.
            if i == 3:  # 4방향을 모두 탐색했을 때 cost 에 인접한 0의 개수를 넣는다.
                cost[x][y] = cnt_0


cnt = 0
while True:
    result = 0  # 빙산이 몇 덩이인지
    cost = [[0] * m for _ in range(n)]  # 해당 빙산의 인접한 0의 개수
    visited = [[False] * m for _ in range(n)]  # 방문 여부
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:  # 빙산이면서 아직 미방문이라면,
                bfs(i, j)
                result += 1
    if result > 1:  # 빙산이 분리되어 있다면,
        print(cnt)
        break
    last = 0
    for i in range(n):
        for j in range(m):
            graph[i][j] -= cost[i][j]  # BFS 탐색 종료 후, cost 값을 graph 에 반영한다.
            if graph[i][j] > 0:  # 남아 있는 빙산의 개수를 센다.
                last += 1
    cnt += 1
    if last == 0:  # 남아있는 빙산의 개수가 0이라면,
        print(0)  # 빙산이 처음부터 끝까지 분리되지 않은 채로 모두 녹았다는 뜻이므로 0을 출력한다.
        break

# 문제 : https://www.acmicpc.net/problem/2573
