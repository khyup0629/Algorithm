# 문제 풀이 아이디어(dfs, dp)
# 1. dfs를 통해 1번 노드부터 리프 노드까지 들어간다.
# 2. 재귀적으로 거슬러 올라오면서 dp 테이블을 갱신한다.
# 3. dp[x][0] : x번 노드가 우수 마을로 선정되지 않았을 때의 x번 노드까지의 마을 주민 수
#    dp[x][1] : x번 노드가 우수 마을로 선정되었을 때의 x번 노드까지의 마을 주민 수
# 4. dp 테이블의 초기값은 초기에 선정되지 않았을 경우 dp[x][0]는 0,
#    주어진 각 노드마다의 마을 주민수가 dp[x][1]로 들어간다.
# 5. x번 노드가 우수 마을로 선정되었을 경우 바로 전 노드(i)가 우수 마을로 선정되지 않은 것이므로 dp[i][0]의 값을 더해준다.
#    dp[x][1] += dp[i][0]
#    x번 노드가 우수 마을로 선정되지 않았을 경우 바로 전 노드(i)가 우수 마을로 선정된 경우와 선정되지 않은 경우 두 경우 중 최댓값을 더한다.
#    dp[x][0] += max(dp[i][0], dp[i][1])
# 6. 1번 노드의 dp값 중 최댓값을 출력한다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

value = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, value[i]] for i in range(n+1)]
visited = [False] * (n + 1)


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            dp[x][1] += dp[i][0]
            dp[x][0] += max(dp[i][0], dp[i][1])


dfs(1)
print(max(dp[1][0], dp[1][1]))

# 문제 : https://www.acmicpc.net/problem/1949
