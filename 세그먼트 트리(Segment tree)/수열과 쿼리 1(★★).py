# 세그먼트 트리와 이진 탐색을 이용한 개수 세기를 결합한 문제였다.
# 문제 풀이 아이디어
# 1. 수열을 세그먼트 트리로 나누는데, 노드의 원소는 구간 내에 들어있는 숫자들이다.
# 2. 각 노드 내에 들어있는 수열들을 오름차순 정렬한다.
# 3. 쿼리를 순서대로 조회하며, k값을 이용해서 bisect_right 이진 탐색을 수행.
# (현재 노드의 수열 길이 - bisect_right) 식을 이용해 개수를 구한다.
# 4. 개수를 리턴하면서 base-case 부터 개수들을 모두 더한다.
from bisect import bisect_right
from math import *
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

h = int(ceil(log2(n)))
t_size = 1 << (h+1)
tree = [[] for _ in range(t_size)]


def init(node, start, end, i, value):

    if not start <= i <= end:
        return
    tree[node].append(value)

    if start == end:
        return

    mid = (start + end) // 2
    init(node*2, start, mid, i, value)
    init(node*2+1, mid+1, end, i, value)


def query(node, start, end, left, right, k):  # 리턴값은 k보다 큰 수의 개수
    if end < left or right < start:  # 범위를 벗어나면 개수는 0
        return 0

    if left <= start and end <= right:  # 범위에 완전히 속하면 개수 계산
        return len(tree[node]) - bisect_right(tree[node], k)

    # 그 외 걸치면 왼쪽, 오른쪽 구간으로 나눠서 들어간다.
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right, k) + query(node*2+1, mid+1, end, left, right, k)


for i in range(n):
    init(1, 0, n-1, i, num[i])

for i in range(len(tree)):
    tree[i].sort()

m = int(input())
for _ in range(m):
    i, j, k = map(int, input().split())
    print(query(1, 0, n-1, i-1, j-1, k))

# 문제 : https://www.acmicpc.net/problem/13537
