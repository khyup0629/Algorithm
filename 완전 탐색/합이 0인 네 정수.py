# 시간 복잡도 O(N^2 + N^2)
# 딕셔너리의 get 함수에 대해 배워볼 수 있었다.
# 또한 이런 류의 문제의 경우 4개의 합을 한꺼번에 고려하기보다
# 2개씩 짝지어서 고려하면 효과적으로 알고리즘을 짤 수 있다는 것을 알았다.

n = int(input())

alist = []
blist = []
clist = []
dlist = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    alist.append(a)
    blist.append(b)
    clist.append(c)
    dlist.append(d)

ab = {}
for a in alist:
    for b in blist:
        # get(key, '디폴트 값')
        # 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값이 반환된다.
        ab[a+b] = ab.get(a+b, 0) + 1

ans = 0
for c in clist:
    for d in dlist:
        ans += ab.get(-c-d, 0)

print(ans)

"""
# DFS 백트래킹 풀이 : 시간 초과 (정확도 O, 효율성 X)
# 시간 복잡도가 O(n^4)라고 볼 수 있었다.

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * 4 for _ in range(n)]
cnt, result = 0, 0


def dfs(y):  # y는 열, x는 행
    global cnt, result
    if y == 4:
        if result == 0:
            cnt += 1
        return
    for x in range(n):
        if not visited[x][y]:
            visited[x][y] = True
            result += array[x][y]
            dfs(y+1)
            result -= array[x][y]
            visited[x][y] = False


dfs(0)
print(cnt)

"""

"""
문제
정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.

A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 배열의 크기 n (1 ≤ n ≤ 4000)이 주어진다. 다음 n개 줄에는 A, B, C, D에 포함되는 정수가 공백으로 구분되어져서 주어진다. 
배열에 들어있는 정수의 절댓값은 최대 228이다.

출력
합이 0이 되는 쌍의 개수를 출력한다.

예제 입력 1 
6
-45 22 42 -16
-41 -27 56 30
-36 53 -37 77
-36 30 -75 -46
26 -38 -10 62
-32 -54 -6 45
예제 출력 1 
5
"""