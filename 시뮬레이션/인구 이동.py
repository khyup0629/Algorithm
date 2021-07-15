# 문제 풀이 아이디어
# 1. BFS로 상하좌우를 탐색해주면서 연합을 만든다.
#  - 탐색하는 동안 연합 회원의 수와 연합의 인구 합, 각 연합 회원국의 위치를 입력받는다.
# 2. 연합 회원국의 위치 정보를 이용해 인구 수를 새로 갱신한다.
# 3. 만약 연합 회원 수가 1일 경우 상하좌우에 국경을 열 나라가 없는 것이므로 end_req += 1
#  - end_req의 값이 전체 나라 수와 같아지면 더이상 인구 이동이 없다는 것을 의미하므로 반복 종료.

from collections import deque
n, L, R = map(int, input().split())

graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)


def bfs(x, y):
    global cnt, hap
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    visited[x][y] = True
    q.append((x, y))
    union.append((x, y))
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):  # 상하좌우 탐색
            nx, ny = now_x + dx[i], now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 지도를 벗어나지 않고,
                if L <= abs(graph[now_x][now_y] - graph[nx][ny]) <= R:  # 인구 이동 조건을 만족하며,
                    if not visited[nx][ny]:  # 아직 방문하지 않았다면, (nx, ny)는 연합이 될 수 있다.
                        visited[nx][ny] = True
                        cnt += 1  # 연합 회원 수 +1
                        hap += graph[nx][ny]  # 연합의 총 인구에 더한다.
                        union.append((nx, ny))  # 연합 나라의 위치를 저장.
                        q.append((nx, ny))


result = 0  # 인구 이동이 발생하는 일수
while True:
    visited = [[False] * n for _ in range(n)]
    end_req = 0  # while문이 끝나기 위한 조건, 더이상 인구이동의 변화가 없다면 이 값은 n * n이 되어야한다.
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt = 1  # 연합 회원의 수
                hap = graph[i][j]  # 연합 인구의 합
                union = []  # 연합 회원의 위치 : (x, y)
                # BFS 탐색을 통해 인구 이동 조건을 만족하는 연합을 형성.
                bfs(i, j)
                if cnt == 1:  # 연합 회원의 수가 1이라면, 현재 (i, j)위치에서 상하좌우로 연합할 나라가 없다는 뜻이므로,
                    end_req += 1
                    continue
                # 연합 회원 수가 2 이상이면, 현재 연합 내에서 인구 이동 후의 값을 갱신한다.
                for pos_x, pos_y in union:
                    graph[pos_x][pos_y] = hap // cnt
    # end_req의 값이 전체 나라 수와 같아지면 더이상 인구 이동이 없다는 것을 의미하므로 반복 종료.
    if end_req == n * n:
        print(result)  # 인구 이동이 발생하는 일수 출력.
        break
    result += 1

# 문제 : https://www.acmicpc.net/problem/16234
