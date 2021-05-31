# 시간 복잡도를 O(N)에서 O(logN)으로 줄이기 위해 세그먼트 트리를 이용했다.

from math import *
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

h = int(ceil(log2(n)))
t_size = 1 << (h+1)
tree = [0] * t_size

num = []
for _ in range(n):
    a = int(input())
    num.append(a)


def init(node, start, end):
    tree[node] = (min(num[start:end+1]), max(num[start:end+1]))
    if start == end:
        return
    mid = (start + end) // 2
    init(node*2, start, mid)
    init(node*2+1, mid+1, end)


def min_max(node, start, end, left, right):  # base-case 의 최솟값과 최댓값을 기록
    if end < left or right < start:  # 구간이 벗어나면 스킵
        return

    if left <= start and end <= right:  # 구간이 완전히 속하면,
        temp.append(tree[node][0])  # 최솟값 추가
        temp.append(tree[node][1])  # 최댓값 추가
        return

    # 구간이 일부만 속하면 왼쪽, 오른쪽으로 쪼개서 들어가기
    mid = (start + end) // 2
    min_max(node*2, start, mid, left, right)
    min_max(node*2+1, mid+1, end, left, right)


init(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    temp = []
    min_max(1, 0, n-1, a-1, b-1)
    print(min(temp), max(temp))

# 문제 : https://www.acmicpc.net/problem/2357
