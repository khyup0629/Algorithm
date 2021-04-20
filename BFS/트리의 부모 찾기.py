# BFS/DFS 문제는 PyPy3로 제출하기

from collections import deque
# 노드의 개수
n = int(input())
# 연결 관계
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
# 방문 여부 리스트
visited = [False] * (n + 1)
# 해당하는 인덱스에 부모 노드를 저장하기 위한 결과값 리스트
result = [0] * (n + 1)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                # result 에 해당하는 인덱스에 부모 노드(x)를 저장
                result[i] = x
                q.append(i)


bfs(1)
# 한 줄에 하나씩 리스트 출력
for i in result[2:]:
    print(i)

"""
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6
"""