# 문제를 잘 따져보면 왼쪽부터 노드 순서가 '중위 순회' 로 이루어짐을 알 수 있다.
# 문제 풀이 아이디어
# 1. 각 노드의 부모 노드를 기록하여 최상단 루트 노드를 찾는다.
# 2. 최상단 노드, 레벨 1부터 시작하는 중위 순회 리스트를 만들고 동시에 각 노드의 레벨을 구한다.
# 3. 중위 순회 리스트를 차례대로 탐색하며 해당 인덱스를 레벨 별로 해시(list)로 정리한다.
# 4. 레벨 1부터 최고 레벨까지 각 레벨 별 해시 리스트의 (마지막 값 - 첫 값 + 1)의 최댓값과 그 때의 레벨을 찾는다.

from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def inorder_depth(node, d):
    if graph[node].left:
        inorder_depth(graph[node].left, d+1)
    num.append(node)
    depth[node] = d
    if graph[node].right:
        inorder_depth(graph[node].right, d+1)


n = int(input())

depth = [0] * (n+1)  # 각 노드의 레벨을 기록할 리스트
parent = [0] * (n+1)  # 최상단 루트 노드를 찾기 위해 노드별 부모 노드 기록
graph = {}
for _ in range(n):
    root, left, right = map(int, input().split())
    if left == -1:
        left = None
    else:
        parent[left] = root
    if right == -1:
        right = None
    else:
        parent[right] = root
    graph[root] = Node(left, right)

# 최상단 루트 노드 찾기
start = 1  # 최상단 루트 노드
while True:
    if parent[start] == 0:
        break
    start = parent[start]

num = []  # 트리의 중위 순회 노드가 기록될 리스트
inorder_depth(start, 1)  # 최상단 루트 노드(start)는 레벨이 1

table = defaultdict(list)  # 레벨 별로 순서대로 인덱스를 담는다.
for i in range(1, n+1):
    table[depth[num[i-1]]].append(i)

_max = 0
idx = 0
for i in range(1, len(table)+1):
    if _max < table[i][-1] - table[i][0] + 1:
        _max = table[i][-1] - table[i][0] + 1
        idx = i  # 같은 max 값이 있을 경우 자연스럽게 레벨이 낮은 번호가 선택됨.

print(idx, _max)

# 문제 : https://www.acmicpc.net/problem/2250
