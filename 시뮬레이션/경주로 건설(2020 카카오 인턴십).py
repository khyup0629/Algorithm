# 시뮬레이션과 BFS가 결합된 문제.
# BFS로도 충분히 비용 문제를 계산할 수 있다.
# 현재 바라보고 있는 방향(dirc)와 나아갈 방향(i)의 관계를 이용한다.
# dirc = i -> 직진(+100), dirc != i -> 직진 후 회전(+100+500)

from collections import deque


def solution(board):
    n = len(board)
    INF = int(1e9)  # 무한대

    # 상:0, 좌:1, 하:2, 우:3
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def bfs(x, y, dirc):
        cost = [[INF] * n for _ in range(n)]
        q = deque()
        cost[x][y] = 0
        # 자료구조 : (x좌표, y좌표, x,y좌표에서의 비용, 현재 바라보고 있는 방향)
        q.append((x, y, cost[x][y], dirc))
        while q:
            now_x, now_y, now_cost, dirc = q.popleft()
            for i in range(4):  # i가 가리키는 것은 방향
                nx, ny = now_x + dx[i], now_y + dy[i]
                # 한 번 탐색했던 칸이라도 다시 탐색하면서 최소 비용을 갱신한다.
                if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                    # i(나아가려는 방향)가 현재 바라보고 있는 방향과 같다면 +100, 다르다면 +600
                    n_cost = now_cost + 100 if i == dirc else now_cost + 100 + 500
                    # 새로운 비용(n_cost)이 기존 비용보다 작으면, 갱신해주고 큐에 추가.
                    if n_cost < cost[nx][ny]:
                        cost[nx][ny] = n_cost
                        q.append((nx, ny, n_cost, i))
        return cost[n - 1][n - 1]

    # 시작점에서 아래(2)로 시작하는 경우와 오른쪽(3)으로 시작하는 경우 중 최소 비용이 결괏값
    answer = min(bfs(0, 0, 2), bfs(0, 0, 3))
    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/67259
