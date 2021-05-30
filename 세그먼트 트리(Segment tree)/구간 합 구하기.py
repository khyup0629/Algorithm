from math import *
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, k = map(int, input().split())

h = int(ceil(log2(n)))  # ceil : 소숫점 자리 올림(math 함수)
cnt = 2 ** h  # 2의 거듭제곱 개수로 맞춰준다.
t_size = 1 << (h+1)  # 트리의 노드 개수
tree = [0] * t_size  # 트리의 노드 번호는 반드시 1 ~ t_size - 1

# 비어있는 칸은 0으로 합을 계산할 때 영향을 주지 않도록 한다.
num = [int(input()) for _ in range(n)]
for i in range(n, cnt):
    num.append(0)


def init(node, start, end):  # build 연산

    if start == end:  # 길이가 1인 구간일 때 tree 값을 기록. 이후로 재귀적으로 거슬러 올라가며 합을 기록.
        tree[node] = num[start]
        return tree[node]

    mid = (start + end) // 2
    # 자식 노드의 합을 부모 노드에 기록
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid+1, end)
    return tree[node]


def update(node, i, diff, start, end):  # 업데이트
    if not start <= i <= end:  # 업데이트 할 원소가 구간에 속하지 않으면 스킵.
        return

    tree[node] += diff  # 업데이트 될 값과 원래 값의 차이만큼 노드 값에 더해준다.

    if start == end:  # 길이 1 구간이면 스킵
        return
    else:  # 길이가 1보다 큰 구간이면 왼쪽, 오른쪽 구간으로 나눠서 진행.
        mid = (start + end) // 2
        update(node * 2, i, diff, start, mid)
        update(node * 2 + 1, i, diff, mid+1, end)


def base_case_sum(node, start, end, left, right):  # base-case 의 합
    if left <= start and end <= right:  # 노드가 b ~ c 구간에 완전히 속해 있는 경우 tree의 값을 반환하고 내려가는 것을 멈춘다.
        return tree[node]

    if end < left or right < start:  # 노드가 b ~ c 구간을 벗어난 경우 0의 값을 반환하고 내려가는 것을 멈춘다.
        return 0

    mid = (start + end) // 2
    # base-case 를 모두 더한다.
    return base_case_sum(node * 2, start, mid, left, right) + base_case_sum(node*2+1, mid+1, end, left, right)


init(1, 0, cnt-1)

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - num[b-1]  # 업데이트 할 값과 원래 값의 차이
        num[b-1] = c  # 업데이트
        update(1, b-1, diff, 0, cnt-1)  # 최상단 노드부터 시작.
    else:
        print(base_case_sum(1, 0, cnt-1, b-1, c-1))

# 문제 : https://www.acmicpc.net/problem/2042
