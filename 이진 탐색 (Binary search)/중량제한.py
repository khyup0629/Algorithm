# 이진 탐색과 BFS를 응용해야 했던 문제였다.
# w값의 범위가 1~1e9 이므로 이를 이진탐색으로 찾는다.
# 먼저 이진 탐색으로 들고 갈 무게(mid)에 대해서 갱신하면서
# 들고 갈 무게(mid)를 BFS에 대입해서 길을 찾는다.
# 만약 미방문 상태의 노드이면서 다리가 견딜 수 있는 무게가 들고 갈 무게(mid)보다 클 경우 다음 노드로 갈 수 있도록 코딩하고,
# BFS 이 완료되었을 때, 목적지 노드가 방문 완료일 경우 True, 미방문일 경우 False를 반환한다.
# True이면 mid값을 결과값으로 넣고, 좀 더 들고 갈 무게를 올려볼 수 있다.

from collections import deque
# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 그래프 그리기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    # 시작(도착) 노드, 도착(시작)노드, 무게 제한
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))
# 출발 노드, 도착 노드
start_node, end_node = map(int, input().split())


def bfs(mid):
    q = deque()
    q.append(start_node)
    visited[start_node] = True
    while q:
        x = q.popleft()
        for y, w in graph[x]:
            # 만약 미방문 상태의 노드이면서 다리가 견딜 수 있는 무게(w)가 들고 갈 무게(mid)보다 클 경우
            if not visited[y] and w >= mid:
                visited[y] = True  # 다음 노드로 간다.
                q.append(y)
    # BFS 이 완료되었을 때, 목적지 노드가 방문 완료일 경우 True, 미방문일 경우 False를 반환한다.
    return True if visited[end_node] else False


result = 1
# w값의 범위가 1~1e9 이므로 이를 이진탐색으로 찾는다.
start, end = 1, int(1e9)
# 이진 탐색으로 들고 갈 무게(mid)에 대해서 갱신
while start <= end:
    # 방문 여부 초기화
    visited = [False] * (n + 1)
    mid = (start + end) // 2
    # bfs가 True라는 것은 mid 의 값으로 목적지까지 도달했다는 뜻
    if bfs(mid):
        result = mid  # 값 기록
        start = mid + 1  # 늘려볼 수 있다.
    else:
        end = mid - 1  # 줄여볼 수 있다.

print(result)

"""
문제
N(2≤N≤10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 
물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다. 
그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다.
만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M(1≤M≤100,000)이 주어진다. 
다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1≤A, B≤N), C(1≤C≤1,000,000,000)가 주어진다. 
이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다. 
서로 같은 두 도시 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다. 
마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다. 
공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
3 3
1 2 2
3 1 3
2 3 2
1 3
예제 출력 1 
3
"""