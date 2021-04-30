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


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


result = 0  # 최소 비용
for edge in graph:
    cost, a, b = edge
    # 서로의 부모 노드가 같지 않다. 즉, 사이클이 발생하지 않는다면
    if find(parent, a) != find(parent, b):
        union(parent, a, b)  # 합집합 수행
        result += cost  # 최소 비용으로 더한다.

print(result)

"""
문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. 
C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 
최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

예제 입력 1 
3 3
1 2 1
2 3 2
1 3 3
예제 출력 1 
3
"""