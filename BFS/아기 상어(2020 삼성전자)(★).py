from collections import deque

n = int(input())

graph = []
for _ in range(n):
    array = list(map(int, input().split()))
    graph.append(array)

visited = [[False] * n for _ in range(n)]  # 방문 여부 테이블
cost = [[int(1e9)] * n for _ in range(n)]  # 무한대 값
shark_size = 2  # 상어의 초기 크기는 2
tim, cnt = 0, 0  # 엄마 부를 때까지 시간, 물고기 먹은 횟수


def bfs(start_x, start_y):  # 현재 위치에서 각 위치까지 최단거리 구하기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    cost[start_x][start_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                cost[nx][ny] = min(cost[nx][ny], cost[x][y] + 1)
                q.append((nx, ny))


# 상어 초기 위치 찾기, 초기 위치가 현재 위치
now_x, now_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            now_x, now_y = i, j
        # 지금 상어보다 사이즈가 큰 물고기는 못 지나가게 막기
        if graph[i][j] > shark_size:
            visited[i][j] = True

while True:
    bfs(now_x, now_y)
    eat = []
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < shark_size:
                eat.append((cost[i][j], i, j))

    if not eat:  # 비었다면 더 이상 먹을 고기가 없다는 뜻
        break

    eat.sort(key=lambda x:(x[0], x[1], x[2]))

    a, now_x, now_y = eat.pop(0)
    if a >= int(1e9):  # a가 무한대란 뜻은 가는 길이 막혔다는 뜻임.
        break
    graph[now_x][now_y] = 0
    tim += a  # 최단거리만큼 결괏값에 더하기
    cnt += 1  # 먹이 먹은 횟수

    # 먹은 횟수가 상어 크기와 같아지면,
    if cnt == shark_size:
        cnt = 0  # 먹은 횟수 초기화
        shark_size += 1  # 상어 크기 +1

    # 새로운 현재 위치에서 다시 최단 거리를 구하기 위한 초기화 작업
    # 현재 상어 크기보다 큰 물고기가 있는 칸은 BFS 할 때 못 지나가게 한다.
    visited = [[False] * n for _ in range(n)]
    cost = [[int(1e9)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > shark_size:
                visited[i][j] = True

print(tim)

# 문제 : https://www.acmicpc.net/problem/16236

"""
예제 입력 7
4
2 4 1 1
0 4 0 0
0 4 9 0
0 4 0 0
예제 출력 7
3
"""