from collections import deque

N = int(input())
K = int(input())

apple = []
for i in range(K):
    x = map(int, input().split(' '))
    apple.append(list(x))

L = int(input())
move_change = []
for i in range(L):
    x = input().split(' ')
    # move_change 의 1항목은 'L' or 'D' 방향 변경
    move_change.append(list(x))

board = [[0 for j in range(N+1)] for i in range(N+1)]

for i in apple:
    x, y = i[0], i[1]
    board[x][y] = 1

# U, D, L, R
direction = [0, 1, 2, 3]
movement = [[-1, 0], [1, 0], [0, -1], [0, 1]]

direction_num = 3
queue = deque([[1, 1]])
x, y = 1, 1
result = 0
changed = 0
i = 0
while True:
    x += movement[direction_num][0]
    y += movement[direction_num][1]
    result += 1
    # 벽에 부딪히거나 자기 몸에 부딪히면 끝
    if x < 1 or x > N or y < 1 or y > N or queue.count([x, y]) == 1:
        break
    queue.append([x, y])
    # 사과가 없으면 큐에서 제외, 사과를 먹으면 0으로
    if board[x][y] == 0:
        queue.popleft()
    else:
        board[x][y] = 0
    for i in range(L):
        if result == int(move_change[i][0]):
            if direction_num == 0:
                if move_change[i][1] == 'L':
                    direction_num = 2
                else:
                    direction_num = 3
            elif direction_num == 1:
                if move_change[i][1] == 'L':
                    direction_num = 3
                else:
                    direction_num = 2
            elif direction_num == 2:
                if move_change[i][1] == 'L':
                    direction_num = 1
                else:
                    direction_num = 0
            elif direction_num == 3:
                if move_change[i][1] == 'L':
                    direction_num = 0
                else:
                    direction_num = 1

print(result)
