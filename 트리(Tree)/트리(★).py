# 전체적인 아이디어는 맞았으나 세부적인 반례를 고려해야 했던 문제
# 1. 연결 리스트로 그래프의 연결을 부모->자식 순으로 단방향으로 기록한다.
# 2. 해시를 이용해 부모:[자식1, 자식2] 형식으로 기록한다.
# 3. 지워야 하는 노드(delete)에서부터 DFS를 통해 연결되어 있는 노드들을 해시에서 지운다.
# 4. 해시 원소들 중 value 가 []인 원소의 갯수를 카운트한다.
# 5. 지워야 하는 노드(delete)의 부모 노드의 자식 노드가 delete 하나 뿐이고, 최상단 부모 노드가 아니면
# delete의 부모 노드 또한 리프 노드(자식 노드가 없는)가 되므로 카운트 +1 한다.
# 부연설명 : 3번 과정에서 delete 위로 부모 노드는 해시에서 지우지 않았기 때문에 delete 의 부모 노드에는 여전히 데이터가 남아있다.
# 따라서, value 가 []가 아니므로 카운트 되지 않기 때문에 따로 카운트 해준다.

import sys
sys.setrecursionlimit(10**5)

n = int(input())

arr = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(n):
    if arr[i] == -1:
        continue
    graph[arr[i]].append(i)

delete = int(input())
visited = [False] * n

result = {}
for i in range(n):
    result[i] = graph[i]


def dfs(delete):
    visited[delete] = True
    del result[delete]
    for i in graph[delete]:
        if not visited[i]:
            dfs(i)


dfs(delete)

cnt = 0
for i in result:
    if result[i] == []:
        cnt += 1

if arr.count(arr[delete]) == 1 and arr[delete] != -1:
    cnt += 1

print(cnt)

# 문제 : https://www.acmicpc.net/problem/1068

"""
반례
입력
5
-1 0 0 1 1
1
출력
1
입력
4
-1 0 0 1
3
출력
2
입력
2
-1 0
1
출력
1
"""