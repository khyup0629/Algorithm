# 문제 풀이 아이디어
# 1. 이진 탐색 기법을 적용하면서 재귀적으로 구할 수 있다.
import sys
sys.setrecursionlimit(10**5)

k = int(input())
order = list(map(int, input().split()))

depth = [[] for _ in range(k)]


def dfs(start, end, d):  # 반으로 나누면서 진행
    mid = (start + end) // 2
    depth[d].append(str(order[mid]))  # join을 이용하기 위해 문자열로 바꿔서 append
    if start == end:
        return
    dfs(start, mid-1, d+1)  # 왼쪽 구간
    dfs(mid+1, end, d+1)  # 오른쪽 구간


dfs(0, 2**k-2, 0)  # 전체 구간부터 시작
for i in range(k):
    print(' '.join(depth[i]))

# 문제 : https://www.acmicpc.net/problem/9934
