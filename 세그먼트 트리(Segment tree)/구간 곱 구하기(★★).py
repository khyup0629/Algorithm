# 각 곱셈 연산마다 1,000,000,007의 나머지를 계산하는 것이 포인트이다.
# 오버 플로우 발생을 방지하여 연산 속도가 빨라진다.

from math import *
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n, m, k = map(int, input().split())

h = int(ceil(log2(n)))
cnt = 2 ** h
t_size = 1 << (h + 1)
tree = [0] * t_size

num = [int(input()) for _ in range(n)]
for i in range(n, cnt):
    num.append(1)


def init(node, start, end):
    if start == end:
        tree[node] = num[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) * init(node * 2 + 1, mid + 1, end) % 1000000007
    return tree[node]


def update(node, i, start, end):  # bottom-up, 업데이트
    if not start <= i <= end:
        return

    if start == end:
        tree[node] = num[start]
    else:
        mid = (start + end) // 2
        update(node * 2, i, start, mid)
        update(node * 2 + 1, i, mid + 1, end)
        tree[node] = tree[node * 2] * tree[node * 2 + 1] % 1000000007


def base_case_mul(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]

    if end < left or right < start:
        return 1

    mid = (start + end) // 2
    return base_case_mul(node * 2, start, mid, left, right) * base_case_mul(node * 2 + 1, mid + 1, end, left, right) \
           % 1000000007


init(1, 0, cnt - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        num[b - 1] = c
        update(1, b - 1, 0, cnt - 1)
    else:
        print(base_case_mul(1, 0, cnt - 1, b - 1, c - 1) % 1000000007)

# 문제 : https://www.acmicpc.net/problem/11505

# 메모리 초과, 누적 합
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

num = [0] + [int(input()) for _ in range(n)]

dp = [1] * (n + 1)
dp[1] = num[1]
for i in range(1, n+1):
    dp[i] = dp[i-1] * num[i]

arr = {}
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b] = c
    else:
        result = dp[c] // dp[b-1]
        for i in arr:
            if i <= c:
                result = (result // num[i]) * arr[i]
        print(result % 1000000007)
