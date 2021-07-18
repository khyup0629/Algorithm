# 문제 풀이 아이디어
# 1. 중심점을 기준으로 90도 회전했을 때의 좌표를 구하는 규칙을 찾는다.
#    (1 -> 2 사분면, 2 -> 3 사분면, 3 -> 4 사분면, 4 -> 1 사분면의 경우가 있다)
# 2. 드래곤 커브에 해당하는 꼭짓점을 따로 저장한다.
# 3. 사각형이 드래곤 커브 꼭짓점이 될 수 있는지를 찾는다.
#    (좌표의 점을 하나씩 완전 탐색하며 (i, j), (i+1, j), (i, j+1), (i+1, j+1)의 4개의 점이
#    모두 드래곤 커브 꼭짓점에 해당하면 개수를 세면 된다)
n = int(input())
cnt = 0
graph = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    point = [(x, y)]  # 현재 드래곤 커브의 꼭짓점이 저장될 장소
    # 맨 처음에 방향(d)으로 0세대 드래곤 커브를 수행한다.
    if d == 0:
        x += 1
    elif d == 1:
        y -= 1
    elif d == 2:
        x -= 1
    else:
        y += 1
    point.append((x, y))
    # 1세대 드래곤 커브부터 g세대까지 수행한다.
    for i in range(g):
        center_x = point[-1][0]
        center_y = point[-1][1]
        for idx in range(len(point)-2, -1, -1):
            nx = point[idx][0]
            ny = point[idx][1]
            dif_x = abs(center_x - nx)
            dif_y = abs(center_y - ny)
            if center_x >= nx and center_y >= ny:  # 4 -> 1
                point.append((center_x + dif_y, center_y - dif_x))
            elif center_x <= nx and center_y >= ny:  # 1 -> 2
                point.append((center_x + dif_y, center_y + dif_x))
            elif center_x <= nx and center_y <= ny:  # 2 -> 3
                point.append((center_x - dif_y, center_y + dif_x))
            elif center_x >= nx and center_y <= ny:  # 3 -> 4
                point.append((center_x - dif_y, center_y - dif_x))
    # 현재 드래곤 커브의 꼭짓점을 모두 한데 모아 저장한다.
    for nx, ny in point:
        graph.append((nx, ny))

# 좌표를 완전 탐색하며 4개의 꼭짓점이 드래곤 커브에 해당하면 개수를 센다.
for i in range(101):
    for j in range(101):
        if (i, j) in graph:
            if (i+1, j) in graph:
                if (i, j+1) in graph:
                    if (i+1, j+1) in graph:
                        cnt += 1
print(cnt)

# 문제 : https://www.acmicpc.net/problem/15685
