# 문제 풀이 아이디어
# 1. 동서남북 네 방향으로 이동할 때 주사위의 전개도가 어떻게 바뀌는지 규칙을 파악한다.
# 2. 임시 저장소(temp)를 두고 전개도의 변경 사항을 저정한다.
# 3. 전개도의 [1][1]이 바닥면, [3][1]이 윗면이다.
dice = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

temp_dice = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

n, m, x, y, k = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
move = list(map(int, input().split()))
for direction in move:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 지도 내에서만 움직임이 가능하다.
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        # 네 방향으로의 움직임에 따라 전개도가 변경되는 규칙
        if direction == 1:
            temp_dice[0][1] = dice[0][1]
            temp_dice[1][0] = dice[1][1]
            temp_dice[1][1] = dice[1][2]
            temp_dice[1][2] = dice[3][1]
            temp_dice[2][1] = dice[2][1]
            temp_dice[3][1] = dice[1][0]
        elif direction == 2:
            temp_dice[0][1] = dice[0][1]
            temp_dice[1][0] = dice[3][1]
            temp_dice[1][1] = dice[1][0]
            temp_dice[1][2] = dice[1][1]
            temp_dice[2][1] = dice[2][1]
            temp_dice[3][1] = dice[1][2]
        elif direction == 3:
            temp_dice[0][1] = dice[3][1]
            temp_dice[1][0] = dice[1][0]
            temp_dice[1][1] = dice[0][1]
            temp_dice[1][2] = dice[1][2]
            temp_dice[2][1] = dice[1][1]
            temp_dice[3][1] = dice[2][1]
        elif direction == 4:
            temp_dice[0][1] = dice[1][1]
            temp_dice[1][0] = dice[1][0]
            temp_dice[1][1] = dice[2][1]
            temp_dice[1][2] = dice[1][2]
            temp_dice[2][1] = dice[3][1]
            temp_dice[3][1] = dice[0][1]
        # 지도 칸이 0일 경우
        if graph[x][y] == 0:
            graph[x][y] = temp_dice[1][1]  # 바닥면 숫자 복사
        # 지도 칸이 0이 아닐 경우
        else:
            temp_dice[1][1] = graph[x][y]  # 지도 칸 숫자를 주사위 바닥면에 복사
            graph[x][y] = 0  # 지도 칸은 0
        # 임시 저장소 -> 주사위 전개도로 값을 옮겨준다.
        dice[0][1] = temp_dice[0][1]
        dice[1][0] = temp_dice[1][0]
        dice[1][1] = temp_dice[1][1]
        dice[1][2] = temp_dice[1][2]
        dice[2][1] = temp_dice[2][1]
        dice[3][1] = temp_dice[3][1]
        print(dice[3][1])  # 주사위 윗면 출력

# 문제 : https://www.acmicpc.net/problem/14499
