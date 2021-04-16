# 2차원 행렬의 인덱스를 선형 인덱스로 만들어서 푼 아이디어
# 선형 인덱스를 이용해 0인 지점을 완전 탐색하고
# 바이러스 감염은 DFS 를 이용

import sys
sys.setrecursionlimit(100000)
# 재귀 제한 해제


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if visited[x][y] == 0:
            visited[x][y] = 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)


n, m = map(int, input().split(' '))

area = [list(map(int, input().split(' '))) for _ in range(n)]

# area 2차원 리스트를 선형 인덱스로 표현함. 각 요소엔 좌표
linear_index = [[0] for _ in range(n*m)]

# 방문 여부 2차원 리스트 생성
visited = [[0 for _ in range(m)] for _ in range(n)]

# 바이러스 감염 스팟 따로 저장, dfs 에 이용
virus_spot = []

# 선형 인덱스를 만들고, 방문 여부 리스트 0, 1로 정리(감염 스팟은 0)
s = 0
for i in range(n):
    for j in range(m):
        linear_index[s] = [i, j]
        if area[i][j] == 1:
            visited[i][j] = 1
        if area[i][j] == 2:
            # 바이러스 감염 스팟을 선형 인덱스로 저장
            virus_spot.append(s)
        s += 1

result = []
for i in range(n*m):
    for j in range(i+1, n*m):
        for k in range(j+1, n*m):
            # 선형 인덱스에 해당하는 area 2차원 리스트 행렬 좌표 (x,y)
            x1, y1 = linear_index[i][0], linear_index[i][1]
            x2, y2 = linear_index[j][0], linear_index[j][1]
            x3, y3 = linear_index[k][0], linear_index[k][1]
            # 탐색하려는 area 의 요소들이 셋 다 0이면
            if not (bool(area[x1][y1]) or bool(area[x2][y2]) or bool(area[x3][y3])):
                visited[x1][y1] = visited[x2][y2] = visited[x3][y3] = 1
                # 바이러스 감염 진행, dfs 이용, 바이러스 감염 스팟부터 탐색
                for a in virus_spot:
                    vx, vy = linear_index[a][0], linear_index[a][1]
                    dfs(vx, vy)
                # 0 개수 세서 결과 리스트에 추가
                count = 0
                for a in visited:
                    count += a.count(0)
                result.append(count)
                # visited 원상태로 초기화
                for a in range(n*m):
                    x0, y0 = linear_index[a][0], linear_index[a][1]
                    if area[x0][y0] == 2:
                        visited[x0][y0] = 0
                    else:
                        visited[x0][y0] = area[x0][y0]

print(max(result))
