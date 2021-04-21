# *를 묶어서 BFS 처리해준 후에 S를 묶어서 BFS 처리
# S가 D에 도착하거나 상하좌우로 갈 곳이 없다면 종료

from collections import deque
# 가로 길이, 세로 길이
n, m = map(int, input().split())
# 맵 입력
graph = [list(input()) for _ in range(n)]
# S와 *의 위치를 구한다.
q = deque()
temp_q = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            start_x, start_y = i, j
        if graph[i][j] == '*':
            temp_q.append([i, j])
# *의 위치는 묶어서 저장한다(2개 이상이 될 수도 있기 때문)
q.append(temp_q)
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    # S에 대한 초기값 설정
    q_s = deque()
    q_s.append([[start_x, start_y]])
    # 카운트 세어주기
    cnt = 0
    while True:
        # *에 대한 상하좌우 처리
        now = q.popleft()
        temp_q = []
        # now 에는 이번 카운트에서의 모든 S의 위치가 저장
        # k는 *의 위치가 [x, y] 형태로 저장되어 있음.
        for k in now:
            x, y = k[0], k[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    # 빈 곳에만 상하좌우로 물이 차도록
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = '*'
                        temp_q.append([nx, ny])
        q.append(temp_q)  # 다음 * 위치들을 묶어서 q에 저장
        # S에 대한 상하좌우 처리
        now = q_s.popleft()
        temp_q_s = []
        changed = 0  # 상하좌우로 S가 움직였는지 판별하기 위한 변수
        # now 에는 이번 카운트에서의 모든 S의 위치가 저장
        # k는 S의 위치가 [x, y] 형태로 저장되어 있음.
        for k in now:
            x, y = k[0], k[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == '.':
                        changed = 1
                        graph[nx][ny] = 'S'
                        temp_q_s.append([nx, ny])
                    # S가 D에 도착하면
                    if graph[nx][ny] == 'D':  # 종료 조건
                        cnt += 1
                        return cnt  # cnt 반환
        q_s.append(temp_q_s)  # S의 위치들을 묶어서 q_s에 저장
        cnt += 1
        # 상하좌우로 갈 곳이 없을 때
        if changed == 0:  # 종료 조건
            return "KAKTUS"


print(bfs())

"""
문제
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고,
그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다. 이 숲에는 고슴도치가 한 마리 살고 있다. 
고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 
비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다.
물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 
또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 
이동할 수 있으면 고슴도치가 물에 빠지기 때문이다. 

입력
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.

다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.

출력
첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다. 
만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.

예제 입력 1 
3 3
D.*
...
.S.
예제 출력 1 
3
예제 입력 2 
3 3
D.*
...
..S
예제 출력 2 
KAKTUS
예제 입력 3 
3 6
D...*.
.X.X..
....S.
예제 출력 3 
6
예제 입력 4 
5 4
.D.*
....
..X.
S.*.
....
예제 출력 4 
4
"""