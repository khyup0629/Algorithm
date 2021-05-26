# 후위 순회에서 제일 마지막 원소는 최초의 부모 노드를 나타낸다.
# 이를 시작으로 중위 순회 리스트에서 후위 순회의 제일 마지막 원소와 같은 노드를 기준으로 왼쪽, 오른쪽으로 나눈다.
# 이때, 중위 순회 리스트를 기준으로 왼쪽과 오른쪽 각각의 원소 갯수를 기록한 후
# 재귀 함수를 통해 start, end 를 왼쪽, 오른쪽 순서로 재귀적으로 들어가며 구하면 된다.

# 중위 순회와 후위 순회의 start, end 를 따로 두어야 하는데 이유는
# 이진 트리의 오른쪽을 탐색할 때 리스트 상으로 중위 순회 원소에 비교해 후위 순회 원소가 앞으로 한 단계씩 밀려있기 때문이다.

import sys
sys.setrecursionlimit(10**5)

n = int(input())

ino = list(map(int, input().split()))  # 중위
pos = list(map(int, input().split()))  # 후위

# ino 리스트에서 각 노드가 위치한 인덱스를 기록.
# ex) 8번 노드가 ino 리스트에서 위치한 인덱스는 1 : index[8] = 1
index = [0] * (n + 1)
for i in range(n):
    index[ino[i]] = i


def preorder(ino_start, ino_end, pos_start, pos_end):
    if ino_start > ino_end or pos_start > pos_end:
        return
    print(pos[pos_end], end=' ')

    # 후위 순회 리스트 부분 구간의 제일 마지막 원소를 기준으로,
    left = index[pos[pos_end]] - ino_start  # 왼쪽 갯수
    right = ino_end - index[pos[pos_end]]  # 오른쪽 갯수

    preorder(ino_start, ino_start + left - 1, pos_start, pos_start + left - 1)  # 왼쪽 구간
    preorder(ino_end - right + 1, ino_end, pos_end - right, pos_end - 1)  # 오른쪽 구간


preorder(0, n-1, 0, n-1)

# 문제 : https://www.acmicpc.net/problem/2263
"""
11
8 4 9 2 5 1 10 6 11 3 7
8 9 4 5 2 10 11 6 7 3 1
"""