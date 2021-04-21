# 모든 간선의 비용이 같은 최단 거리 문제 : BFS 사용 가능
from collections import deque
# 전체 층수, 현재 층, 도착 층, 올라갈 수 있는 층, 내려갈 수 있는 층
F, S, G, U, D = map(int, input().split())
# 방문 여부 리스트
visited = [False] * (F + 1)
# 위, 아래
dx = [U, -D]
# 각 층을 인덱스로 하는 최단 거리 리스트 생성
# 메모리를 줄이기 위해 아직 갱신되지 않은 층은 -1
dist = [-1 for _ in range(F+1)]
# 시작 층의 최단 거리는 0
dist[S] = 0


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            if 0 < nx <= F:
                if not visited[nx]:
                    visited[nx] = True
                    # 갈 수 있는 최단 경로 갱신
                    dist[nx] = dist[x] + 1
                    q.append(nx)


bfs(S)
print(dist[G] if dist[G] != -1 else "use the stairs")

"""
문제
강호는 코딩 교육을 하는 스타트업 스타트링크에 지원했다. 오늘은 강호의 면접날이다. 
하지만, 늦잠을 잔 강호는 스타트링크가 있는 건물에 늦게 도착하고 말았다.

스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다. 
강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.

보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 강호가 탄 엘리베이터는 버튼이 2개밖에 없다. 
U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다. 
(만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오. 
만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.

입력
첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.

출력
첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다. 
만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력한다.

예제 입력 1 
10 1 10 2 1
예제 출력 1 
6
예제 입력 2 
100 2 1 1 0
예제 출력 2 
use the stairs
"""
"""
# 전체 층수, 현재 층, 도착 층, 올라갈 수 있는 층, 내려갈 수 있는 층
F, S, G, U, D = map(int, input().split())

cnt = 0
while True:
    changed = S  # 기존 S값 기록
    if S < G:
        S += U
        # 최고 층보다 넘어가게 되면 원래 S에서 D를 뺀다
        if S > F:
            S = changed - D
            # 이 S값이 1층 밑으로 내려간다면 엘리베이터를 이용할 수 없다.
            if S < 1:
                print("use the stairs")
                break
    else:
        S -= D
        if S < 1:
            S = changed + U
            if S > F:
                print("use the stairs")
                break
    cnt += 1
    # 층수가 변하지 않거나
    # U와 D가 같으면 계속 맴돌게 되므로 엘리베이터를 이용할 수 없다.
    if changed == S or U == D:
        print("use the stairs")
        break
    # 도착 층에 도착하면 cnt 출력하고 반복 종료.
    if S == G:
        print(cnt)
        break
"""