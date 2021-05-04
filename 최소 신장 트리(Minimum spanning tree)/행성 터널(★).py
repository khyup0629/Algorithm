# 메모리/시간 초과가 나지 않게 하려면 간선을 줄이는 방법을 생각해야 한다.
# 꼭 모든 간선을 구할 필요가 없다.
# 모든 간선이 아닌 각 좌표별로 거리를 구하면 간선의 개수를 현저히 줄일 수 있다.
# 기존 방식은 V * (V - 1) / 2의 간선을 추가하는데,
# 좌표별로 정렬해서 간선을 구하면 X1 -> X2가 X1 -> X3보다 클 수 없기 때문에
# 3 * (V - 1)의 간선이 추가되어 간선을 효과적으로 줄일 수 있다.

# 그런데 솔직히 이해가 잘 되지 않는다.
# 위의 방식대로 구할 경우 어떤 노드 사이의 간선의 비용이 온전히 구해지지 않는 경우도 생기는데
# 어떻게 위의 방식이 정답이 될 수 있는지...
# 모든 노드가 연결이 되어 있기 때문에 가능한 것일지도...
# 노드가 어떤 식으로 연결될 지는 여러가지 답이 존재할 것이고
# 그 중에서 최소한의 간선을 구하는 방법일지도 모르겠다.
# 최소한으로 구해진 간선이 모든 노드의 연결을 사이클 없이 보장하게 되는 것이다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

parent = [i for i in range(n)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a


# 노드 번호 별 좌표 저장 (0 ~ n-1)
cor = [0] * n
for a in range(n):
    x, y, z = map(int, input().split())
    # (x, y, z, 노드 번호)
    cor[a] = (x, y, z, a)

# x, y, z 좌표에 대해 각각 정렬한 후 간선 구하기
graph = []
for i in range(3):
    cor.sort(key=lambda x:x[i])
    for j in range(1, n):
        # (비용, 첫 번째 노드, 두 번째 노드)
        graph.append((abs(cor[j][i] - cor[j-1][i]), cor[j][3], cor[j-1][3]))

graph.sort()

result = 0
for cost, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)
