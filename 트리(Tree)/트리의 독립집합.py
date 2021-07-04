# '우수 마을' 문제에서 최대 가중치를 계산할 때 쓰인 노드들까지 출력해야하는 문제이다.
# 문제 풀이 아이디어
# 1. 노드를 담는 3차원 배열을 만들어서 dp 테이블의 가중치를 갱신할 때 따라서 갱신한다.
#    dp[x][1] 을 갱신할 때 : node[i][0]에 담겨있는 노드들을 node[x][1]에 추가해준다.
#    dp[x][0] 을 갱신할 때 : dp[i][0], dp[i][1] 둘 중 큰 값에 따라 node[i][0], node[i][1]에 담겨있는 노드들을 node[x][0]에 추가.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())

w = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)
dp = [[0, w[i]] for i in range(n+1)]
visited = [False] * (n + 1)
node = [[[], [i]] for i in range(n+1)]  # 노드들이 저장될 공간
# 현재 노드를 선택할 때 이전 노드(i)의 선택하지 않았을 때의 값인 dp[i][0]을 더하므로
# dp[x][1] += dp[i][0]
# node[x][1] += node[i][0]
# 를 해주면 이전 노드까지의 선택된 노드들의 정보가 node[x][1]에 추가된다.


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            dp[x][1] += dp[i][0]  # 현재 노드를 선택했을 때
            node[x][1] += node[i][0]
            # 현재 노드를 선택하지 않았을 때
            if dp[i][0] > dp[i][1]:  # 이전 노드를 선택하지 않았을 때
                dp[x][0] += dp[i][0]
                node[x][0] += node[i][0]
            else:  # 이전 노드를 선택했을 때
                dp[x][0] += dp[i][1]
                node[x][0] += node[i][1]


dfs(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    node[1][0].sort()  # 오름차순 정렬 후 출력
    for i in node[1][0]:
        print(i, end=' ')
else:
    print(dp[1][1])
    node[1][1].sort()
    for i in node[1][1]:
        print(i, end=' ')

# 문제 : https://www.acmicpc.net/problem/2213
