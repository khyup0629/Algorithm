from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# index와 노드 번호를 효과적으로 연결짓기 위해 일부러 0번째는 비워둔다
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# index와 노드 번호를 효과적으로 연결짓기 위해
# 노드는 8개이지만 9를 곱해서 인덱스를 0~9까지 만들어준다
# 방문하지 않았으면 False, 방문했으면 True
visited = [False] * 9

bfs(graph, 1, visited)
