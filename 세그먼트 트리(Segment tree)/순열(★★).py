# 문제 풀이 아이디어 : 구간마다 비어있는 칸의 개수를 세그먼트 트리로 나타낸다.
# 1. A 수열의 1번째부터 순서대로 보면, 현재 수 앞에 있는 비어있는 칸의 개수와 같은 것을 알 수 있다.
# 2. 비어있는 칸을 1로 하면 개수를 셀 수 있고, 이를 바탕으로 비어 있는 칸의 개수만큼 구간 합 세그먼트 트리를 만든다.
# 세그먼트 트리의 각 노드값은 현재 구간의 비어있는 칸의 개수를 나타낸다.
# 3. 1번째 수부터 query 함수에 넣고, Top-Down 방식으로 현재 노드의 트리값을 -1하면서 내려간다.
# 4. 왼쪽 자식 노드의 값(왼쪽 구간의 비어있는 칸의 개수)보다 A[i]가 클 경우, 오른쪽 자식 노드로 가게 한다.
# 작거나 같다면 왼쪽 자식 노드로 내려간다. 이를 재귀적으로 query 함수를 구현한다.
# query 함수는 update 의 역할도 수행하는데 리프 노드의 값이 1에서 0으로 바뀌면 그 위치에 값이 채워졌다는 의미이고,
# Top-down 으로 내려오면서 -1을 진행했기 때문에 자연스럽게 위의 부모 노드들 역시 update 가 반영되었다고 볼 수 있다.
# 5. 리프 노드가 1에서 0으로 바뀔 때 start 값을 반환하여 답이 기록될 수열인 L 리스트의 해당 start 위치에 i를 넣는다.
from math import *
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

A = [int(input()) for _ in range(n)]

h = int(ceil(log2(n)))
t_size = 1 << (h+1)
tree = [0] * t_size
L = [0] * n  # 답이 저장될 수열


def init(node, start, end):
    if start == end:
        tree[node] = 1
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]


def query(node, start, end, cnt):
    tree[node] -= 1

    if start == end:
        return start

    mid = (start + end) // 2
    if tree[node*2] > cnt:
        return query(node*2, start, mid, cnt)
    return query(node*2+1, mid+1, end, cnt-tree[node*2])


init(1, 0, n-1)
for i in range(1, n+1):
    idx = query(1, 0, n-1, A[i-1])
    L[idx] = i

for i in L:
    print(i)

# 문제 : https://www.acmicpc.net/problem/1849
