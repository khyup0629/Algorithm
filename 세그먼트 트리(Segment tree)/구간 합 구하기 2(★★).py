# Segment Tree Lazy Propagation 를 이용하는 문제이다.
# 변경되는 원소가 하나가 아닌 '구간' 일 경우 Lazy Propagation 을 이용한다.
# 자세한 설명은 README 를 참고하자.
from math import *
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, k = map(int, input().split())

h = int(ceil(log2(n)))
t_size = 1 << (h+1)
tree = [0] * t_size
lazy = [0] * t_size  # lazy 값.

num = [int(input()) for _ in range(n)]


def init(node, start, end):
    if start == end:
        tree[node] = num[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]


def update_lazy(node, start, end):  # 현재 노드에 남아있는 lazy 값을 tree 값에 더해준다.
    if lazy[node] != 0:
        tree[node] += (end-start+1) * lazy[node]
        if start != end:  # 리프 노드가 아니면,
            lazy[node*2] += lazy[node]  # 자식 노드에게 lazy 값을 물려준다.
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0  # 초기화


def update(node, d, start, end, left, right):
    # 현재 노드에 남아 있는 lazy 값을 tree 값에 더해주고 초기화한다.
    # update 의 update_lazy 는 새로운 lazy 값을 받기 위함이다.
    update_lazy(node, start, end)
    if end < left or right < start:  # 전혀 속하지 않으면 스킵
        return

    if left <= start and end <= right:  # 완전히 속하면,
        tree[node] += (end-start+1) * d
        if start != end:  # 리프 노드가 아니면,
            lazy[node*2] += d  # 자식 노드에게 물려준다.
            lazy[node*2+1] += d
    else:  # 일부만 속하면,
        mid = (start + end) // 2
        update(node*2, d, start, mid, left, right)
        update(node*2+1, d, mid+1, end, left, right)
        tree[node] = tree[node*2] + tree[node*2+1]


def base_case_sum(node, start, end, left, right):
    # 현재 노드에 남아 있는 lazy 값을 tree 값에 더해주고 이를 합에 반영하기 위함으로 update_lazy 를 쓴다.
    update_lazy(node, start, end)
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return base_case_sum(node*2, start, mid, left, right) + base_case_sum(node*2+1, mid+1, end, left, right)


init(1, 0, n-1)

for _ in range(m+k):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        update(1, arr[3], 0, n-1, arr[1]-1, arr[2]-1)
    else:
        print(base_case_sum(1, 0, n-1, arr[1]-1, arr[2]-1))

# 문제 : https://www.acmicpc.net/problem/10999
