N = int(input())

movement = input().split(' ')

# 평소 생각하듯이 x, y 좌표라고 생각하면 안돼
# 세로가 x, 가로가 y
# 오른, 위, 왼, 아래
direction = ['R', 'U', 'L', 'D']
direction_x = [0, -1, 0, 1]
direction_y = [1, 0, -1, 0]
x, y = 1, 1

for i in movement:
    for j in range(len(direction)):
        if direction[j] == i:
            nx = x + direction_x[j]
            ny = y + direction_y[j]
    # nx, ny는 임시 x, y 좌표
    # 공간을 벗어나면 무시
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x = nx
    y = ny

print(x, y)
