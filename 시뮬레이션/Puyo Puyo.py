# BFS 이용

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, flag):
    q = deque()
    # 방문/미방문 여부 2차원 리스트, 방문 여부 초기화
    c = [[0]*6 for _ in range(12)]
    q.append([x, y])
    cnt = 1
    c[x][y] = 1
    # 네 방향 탐색
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                # 지금 위치한 곳과 탐색할 곳이 색이 같고 방문하지 않았다면
                if a[nx][ny] == a[x][y] and c[nx][ny] == 0:
                    # 카운트 +1, 방문 완료 처리
                    cnt += 1
                    c[nx][ny] = 1
                    q.append([nx, ny])
    # 같은 색 뿌요가 4개 이상 붙어있다면 0이 아닌 값을 반환
    # 현재 위치와 붙어있는 같은 색의 뿌요들을 '.'으로 만듦.
    if cnt >= 4:
        flag += 1
        for i in range(12):
            for j in range(6):
                if c[i][j] == 1:
                    a[i][j] = '.'
    return flag


def check_fall():
    # 행의 끝에서부터 위로 탐색
    for i in range(10, -1, -1):
        for j in range(6):
            # 뿌요 밑에 공간이 한 칸이라도 비었다면,
            if a[i][j] != '.' and a[i+1][j] == '.':
                for k in range(i+1, 12):
                    # 끝에서부터 탐색했을 때 처음 나오는 뿌요를 제일 밑으로 내린다.
                    if k == 11 and a[k][j] == '.':
                        a[k][j] = a[i][j]
                    # i 다음부터(i+1) 탐색하면서 처음으로 뿌요가 나왔을 때
                    # 그 전(k-1)로 지금 i행값을 땡겨온다.
                    elif a[k][j] != '.':
                        a[k-1][j] = a[i][j]
                        break
                # 뿌요를 내렸으니 현재 위치한 곳을 비운다(.)
                a[i][j] = '.'


a = [list(input()) for _ in range(12)]

turn = 0  # 연쇄 횟수
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if a[i][j] != '.':
                # 한 번이라도 BFS 를 거치면 cnt >= 1
                cnt = bfs(i, j, cnt)
    # cnt = 0 이면 없어질 뿌요가 없다는 뜻, 반복 종료
    if cnt == 0:
        print(turn)
        break
    turn += 1
    # 중력에 의해 떨어진다
    check_fall()

"""
import sys
sys.setrecursionlimit(100000)
# 재귀 제한 해제

n, m = 12, 6
# 뿌요 입력받기
frame = [list(input()) for _ in range(n)]
print(frame)
# frame 을 숫자화한 리스트 visited 생성
visited = [[0 for _ in range(m)] for _ in range(n)]
# . : 0, R : 1, G : 2, B : 3, P : 4, Y : 5
for i in range(n):
    for j in range(m):
        if frame[i][j] == 'R':
            visited[i][j] = 1
        elif frame[i][j] == 'G':
            visited[i][j] = 2
        elif frame[i][j] == 'B':
            visited[i][j] = 3
        elif frame[i][j] == 'P':
            visited[i][j] = 4
        elif frame[i][j] == 'Y':
            visited[i][j] = 5


def dfs_count(x, y, z):
    global count
    if 0 <= x < n and 0 <= y < m:
        if visited[x][y] == 0:
            return False
        if visited[x][y] == z:
            visited[x][y] = 0
            temp_visited[x][y] = z
            temp_visited_cor.append([x, y])
            count += 1
            dfs_count(x - 1, y, z)
            dfs_count(x + 1, y, z)
            dfs_count(x, y - 1, z)
            dfs_count(x, y + 1, z)


turn = 0
while True:
    print(visited)
    changed = 0
    for i in range(n):
        for j in range(m):
            # 같은 색 뿌요가 붙어있는 개수 세기
            # 초기화
            count = 0
            temp_visited = [[0 for _ in range(m)] for _ in range(n)]
            temp_visited_cor = []
            dfs_count(i, j, visited[i][j])
            # 붙어있는 뿌요가 4개 미만이면 임시 저장소에 저장했던 값을 다시 적용
            if count < 4:
                print(temp_visited_cor)
                for a in temp_visited_cor:
                    temp_x, temp_y = a[0], a[1]
                    visited[temp_x][temp_y] = temp_visited[temp_x][temp_y]
            else:
                # changed 가 1이 된단 뜻은 연쇄가 한 번 이상 일어났다는 뜻
                changed = 1
    # 이번 턴에 연쇄가 한 번도 일어나지 않았다면
    if changed == 0:
        break
    # 한 번의 연쇄
    turn += 1
    # 중력에 의해 비어있는 칸만큼 내려오기 (잘못된 부분)
    for j in range(m):
        # 임시 열 데이터 저장
        temp_col = []
        for i in range(1, n):
            if visited[i][j] != 0:
                # 열 기준으로 0이 아닌 데이터 저장
                temp_col.append(visited[i][j])
                # 열을 임시 초기화
                visited[i][j] = 0
        # 비어있는 칸 만큼 내림
        for i in range(len(temp_col)):
            # visited 행렬의 끝행에서부터 차례대로
            # 임시 열 데이터 저장 행렬의 끝 데이터부터 넣는다.
            visited[n-i-1][j] = temp_col[-(i+1)]

print(turn)

"""
"""
예제 입력 1 
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.
예제 출력 1 
3

예제 입력 2
......
......
......
......
......
......
......
......
......
......
......
......
예제 출력 2
0

......
......
......
......
......
......
......
..G...
.YY...
.BY...
RRYG..
RRYGG.
예제 출력 3
2

RRRRRR
PRBBRR
PRRRRR
PRRRRR
RBBRRR
RPRGGR
RRRRRR
RRGGRR
RRRRRR
RRRRRR
RRRRRR
RRRRRR
2
"""
