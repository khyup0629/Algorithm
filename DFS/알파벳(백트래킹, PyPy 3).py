# 백트래킹을 활용해야 하는 문제, 그런데 계산 시간이 너무 오래 걸려
# 알파벳은 26개 중에서 C개 사용 가능
# PyPy3 로 제출하니 시간 초과 안 뜸.
import sys
sys.setrecursionlimit(100000)
# 재귀 제한 해제


def dfs(x, y, count):
    global result
    # 최대한 들어간 곳까지의 count 를 저장
    result = max(result, count)
    # 4방향 고려
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # frame 을 벗어나지 않으면
        if 0 <= nx < R and 0 <= ny < C:
            # 방문하지 않았으면
            if visited[frame[nx][ny]] == 0:
                visited[frame[nx][ny]] = 1
                # (nx, ny)를 시작점으로 다시 고려
                dfs(nx, ny, count+1)
                # 현재 위치한 노드의 방문 기록을 초기화하면서 뒤로 돌아간
                visited[frame[nx][ny]] = 0  # 백트래킹


R, C = map(int, input().split(' '))
# 알파벳을 방문 리스트의 인덱스와 맞춰주기 위해 ord(x)-65 해서 숫자화
frame = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]

# 방문완료 1, 미방문 0, 알파벳 기준, 알파벳 총 개수 26개
visited = [0] * 26
# 초기값 설정, (0,0)에 있는 알파벳은 방문 완료 처리, 시작점도 개수에 카운트하므로 1
visited[frame[0][0]] = 1
result = 1
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0, result)
print(result)

"""
3 5
CBABE
ADCBE
EEDBE

3 5
CBABA
BBBBA
BBEDA
"""
