# 입력값의 범위를 고려해보았을 때 충분히 완전 탐색으로 구현이 가능했다.
# 문제에서 요구하는 순서대로 코드를 구현하면 된다.
import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())

graph = []
for _ in range(r):
    arr = list(map(int, input().split()))
    graph.append(arr)

machine = []  # 공기청정기의 위치(행) 기록(공기청정기는 무조건 1열에 있다)
for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            machine.append(i)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(t):
    # 1. 미세먼지 확산
    # 미세먼지 확산은 한 번에 일어나므로 모든 증감을 기록할 수 있는 임시 저장소를 만든다.
    temp_graph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:  # 공기청정기가 아닌 곳
                cnt = 0  # 확산된 방향의 개수
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < r and 0 <= nj < c:  # 칸을 벗어나지 않을 때,
                        if graph[ni][nj] != -1:  # 공기청정기 위치가 아닐 때,
                            cnt += 1  # 확산된 방향의 개수
                            temp_graph[ni][nj] += (graph[i][j] // 5)  # 인접 칸 미세먼지 증가
                temp_graph[i][j] -= (graph[i][j] // 5) * cnt  # 현재 칸 미세먼지 감소
    for i in range(r):
        for j in range(c):
            graph[i][j] += temp_graph[i][j]  # 현재 케이스의 미세먼지 증감을 반영한다.
    # 2. 공기청정기 작동(한 칸씩 당기기)
    # 상단 부분 바람 순환, 공기청정기로 들어가는 줄부터
    for i in range(machine[0]-1, 0, -1):  # ↓
        graph[i][0] = graph[i-1][0]
    for i in range(c-1):  # ←
        graph[0][i] = graph[0][i+1]
    for i in range(machine[0]):  # ↑
        graph[i][c-1] = graph[i+1][c-1]
    for i in range(c-1, 0, -1):  # →
        graph[machine[0]][i] = graph[machine[0]][i-1]
    graph[machine[0]][1] = 0  # 공기청정기 오른쪽 칸은 미세먼지 0
    # 하단 부분 바람 순환, 공기청정기로 들어가는 줄부터
    for i in range(machine[1]+1, r-1):  # ↑
        graph[i][0] = graph[i+1][0]
    for i in range(c-1):  # ←
        graph[r-1][i] = graph[r-1][i+1]
    for i in range(r-1, machine[1], -1):  # ↓
        graph[i][c-1] = graph[i-1][c-1]
    for i in range(c-1, 0, -1):  # →
        graph[machine[1]][i] = graph[machine[1]][i-1]
    graph[machine[1]][1] = 0

# 미세먼지의 양 출력
result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)

# 문제 : https://www.acmicpc.net/problem/17144
