# N의 입력 최대 개수가 100,000 이므로 O(N^2)의 시간복잡도를 가지면 안됨
#

n = int(input())

dist = list(map(int, input().split(' ')))
# 방문/미방문 여부
visited = [False] * (n-1)

cost = list(map(int, input().split(' ')))

result = 0
# 이중 for 문을 쓰되 시간 복잡도가 O(N^2)가 되지는 않는다.
for i in range(n-1):
    dist_sum = dist[i]
    if visited[i]:
        continue
    for j in range(i+1, n):
        if cost[i] > cost[j] or j == (n-1):
            result += cost[i] * dist_sum
            break
        else:
            dist_sum += dist[j]
            visited[j] = True

print(result)
