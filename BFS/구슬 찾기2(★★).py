from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    lst = list(input())
    graph.append(lst)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# R과 B의 좌표 찾기
pos_R, pos_B = (0, 0), (0, 0)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            pos_R = (i, j)
        if graph[i][j] == 'B':
            pos_B = (i, j)
# 4차원으로 나타낸 방문 여부 리스트, [R의 x좌표][R의 y좌표][B의 x좌표][B의 y좌표]
# R과 B의 위치에 따라 경우를 고려했는지
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]


def move(x, y, dx, dy):
    cnt = 0  # 몇 칸을 움직였는지
    # 다음 칸이 벽이거나 현재 칸이 O일 때까지 반복
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs(srx, sry, sbx, sby):
    q = deque()
    q.append((srx, sry, sbx, sby, 1))
    visited[srx][sry][sbx][sby] = True
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:  # 기울인 횟수가 10번을 넘어가면 -1 출력
            print(-1)
            return
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if graph[nbx][nby] != 'O':  # B가 O에 들어가지 않은 경우
                if graph[nrx][nry] == 'O':  # R이 O에 들어간 경우
                    print(depth)
                    return
                if nrx == nbx and nry == nby:  # R과 B가 겹친 경우
                    if rcnt > bcnt:  # 둘 중에 더 많은 칸을 움직인 구슬이 움직인 방향의 반대로 후진한다.
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:  # R과 B의 위치가 아직 고려되지 않은 경우
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)  # O에 R과 B가 동시에 들어간 경우


bfs(pos_R[0], pos_R[1], pos_B[0], pos_B[1])

# 문제 : https://www.acmicpc.net/problem/13460
