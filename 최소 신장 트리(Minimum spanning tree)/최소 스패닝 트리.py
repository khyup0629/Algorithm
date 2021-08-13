# 전형적인 최소 신장 트리 문제이다. 간선의 방향이 없고 모든 노드를 연결하는 부분 그래프 중 최소 비용을 구하는 문제이다.
# 계산 시간은 graph.sort() 할 때만 오래 소요되므로 간선의 개수가 E라면
# 시간 복잡도는 O(ElogE)가 된다.
# 따라서 입력값의 범위가 상당히 크더라도 충분히 빠른 계산을 수행할 수 있다.

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 정점의 개수, 간선의 개수
v, e = map(int, input().split())

# 간선 정보 입력
graph = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

# 간선 정보를 비용순으로 오름차순 정렬
graph.sort()

# 부모 노드 초기화(자기 자신을 가리키도록)
parent = [i for i in range(v+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a


result = 0  # 최소 비용
for cost, a, b in graph:
    # 서로의 부모 노드가 같지 않다. 즉, 사이클이 발생하지 않는다면
    if find(a) != find(b):
        union(a, b)  # 합집합 수행
        result += cost  # 최소 비용으로 더한다.

print(result)

# 문제 : https://www.acmicpc.net/problem/1197
