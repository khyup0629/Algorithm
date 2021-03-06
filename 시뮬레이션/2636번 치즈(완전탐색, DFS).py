# 안쪽에 있는 0과 치즈 가장 자리 바깥에 있는 0을 서로 다르게 구분지어 주는 것이 포인트
# 1. 치즈 바깥의 0을 모두 2로 만들어주며 구분지어준다.
# 2. 그 다음 가장자리와 인접한 1을 0으로 만든다.
# 3. 2를 모두 0으로 만들어준 다음 다시 1의 과정으로 돌아가 반복 계산.
# 4. 1이 모두 없어지면 반복 계산 종료.

import sys
sys.setrecursionlimit(100000)
# 재귀 제한 해제

n, m = map(int, input().split(' '))

cheese = [list(map(int, input().split(' '))) for _ in range(n)]

# 치즈의 겉에 있는 부분들을 모두 2로 만들어준다.
def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if cheese[x][y] == 0:
            cheese[x][y] = 2
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)


result_count = []  # 남아 있는 1의 개수 저장소
turn = 0  # 반복 계산 횟수
while True:
    # changed 의 역할은 치즈가 남아있지 않을 때 반복문을 종료하기 위함
    changed = 0
    # 치즈 바깥 가장자리의 0을 모두 2로 만들기
    dfs(0, 0)

    # 남아 있는 1의 개수를 result_count 리스트에 저장
    count = 0
    for i in cheese:
        count += i.count(1)
    result_count.append(count)

    # 1의 상하좌우에 2가 있다면 1 -> 0 으로 만듦.
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                # 1이 남아있다면 반복문을 종료하지 않기 위함.
                changed = 1
                # 상하좌우에 2가 있는지
                if cheese[i-1][j] == 2 or cheese[i+1][j] == 2 or cheese[i][j-1] == 2 or cheese[i][j+1] == 2:
                    cheese[i][j] = 0
    # 1이 남아있지 않다면 반복문 종료.
    if changed == 0:
        break
    # 행렬 중에 2인 부분을 전부 0으로 만들어준다.
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 2:
                cheese[i][j] = 0
    # 반복 계산 횟수 +1
    turn += 1

print(turn)
# 리스트에서 인덱스를 (-)로 하면 뒤에서부터 순서대로
# 리스트에 원소가 1개인 상태라면 0과 -1이 가리키는 원소가 같다.
print(result_count[turn-1])

"""
문제
아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다. 
판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 
치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다. 
<그림 1>의 경우, 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어져서 <그림 2>와 같이 된다.

다시 한 시간 후에는 <그림 2>에서 ‘c’로 표시된 부분이 녹아 없어져서 <그림 3>과 같이 된다.

<그림 3>은 원래 치즈의 두 시간 후 모양을 나타내고 있으며, 남은 조각들은 한 시간이 더 지나면 모두 녹아 없어진다. 
그러므로 처음 치즈가 모두 녹아 없어지는 데는 세 시간이 걸린다. <그림 3>과 같이 치즈가 녹는 과정에서 여러 조각으로 나누어 질 수도 있다.

입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 
공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 
모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 
세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 
둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.

예제 입력 1 
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
예제 출력 1 
3
5
예제 입력 2
3 3
0 0 0
0 1 0
0 0 0
예제 출력 2
1
1
"""