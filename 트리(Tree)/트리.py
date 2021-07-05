# 문제 풀이 아이디어
# 1. 전위 순회 리스트를 앞에서부터 탐색하며 해당 원소의 중위 순회 리스트의 인덱스를 본다.
# 2. 인덱스를 기준으로 왼쪽, 오른쪽 구간으로 나누며 재귀적으로 들어간다.
# 3. 왼쪽, 오른쪽 구간을 모두 탐색하고 나면 마지막에 해당 노드를 출력한다.
import sys

sys.setrecursionlimit(10 ** 5)
t = int(input())


def postorder(start, end):
    global cnt
    if start > end:
        return
    # 재귀 함수(postorder)가 return 되지 않고 호출될 때마다 전위 순회 리스트에서 다음 원소를 탐색해야하므로
    # return 뒤에 cnt += 1을 둔다.
    cnt += 1  # 전위 순회 리스트를 앞에서부터 탐색

    stand = preorder[cnt]  # 현재 탐색중인 전위 순회 리스트 원소
    # 중위 순회에서 현재 탐색 중인 전위 순회 원소의 중위 순회 인덱스를 기준으로 왼쪽, 오른쪽 구간으로 나눠서 재귀함수 호출
    postorder(start, idx_in[stand] - 1)
    postorder(idx_in[stand] + 1, end)
    result.append(str(stand))  # 후위 순회 저장


for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    # 중위 순회 리스트의 각 원소에 해당하는 인덱스 값을 저장
    idx_in = [0] * (n + 1)
    for i in range(n):
        idx_in[inorder[i]] = i
    result = []  # 후위 순회가 저장될 공간
    cnt = -1  # 전위 순회 원소를 인덱스 0부터 탐색하기 위해 -1부터 시작
    postorder(0, n - 1)
    print(' '.join(result))

# 문제 : https://www.acmicpc.net/problem/4256
