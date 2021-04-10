'''
행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면입니다.
왕실 정원의 특정한 한 칸에 나이트가 서 있습니다.
나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며
정원 밖으로는 나갈 수 없습니다.

나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는
경우의 수를 출력하는 프로그램을 작성하세요.
왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며,
열 위치를 표현할 때는 a부터 h로 표현합니다.
c2에 있을 때 이동할 수 있는 경우의 수는 6가지입니다.

입력 조건 : 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표
출력 조견 : 경우의 수

입력 예시
a1
출력 예시
2
'''

position = input()
row = ['1', '2', '3', '4', '5', '6', '7', '8']
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# RU(Right Up), RD, UL, UR, LU, LD, DL, DR
direction_x = [-1, 1, -2, -2, -1, 1, 2, 2]
direction_y = [2, 2, -1, 1, -2, -2, -1, 1]

result = 0

x = row.index(position[1])
y = col.index(position[0])

for i in range(8):
    nx = x + direction_x[i]
    ny = y + direction_y[i]
    if nx < 0 or nx > 8 or ny < 0 or ny > 8:
        continue
    result += 1

print(result)
