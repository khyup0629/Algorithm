# N의 입력 최대 개수가 100,000 이므로 O(N^2)의 시간복잡도를 가지면 안됨
# 현재 도시와 현재 바로 다음 도시들을 차례대로 1대1 비교하면서
# 비용을 비교해 현재 도시 비용이 더 작으면 거리를 누적
n = int(input())
# 도시 사이의 거리
dist = list(map(int, input().split(' ')))
# 방문/미방문 여부
visited = [False] * (n-1)
# 1리터 당 기름값
cost = list(map(int, input().split(' ')))

result = 0
# 이중 for 문을 쓰되 시간 복잡도가 O(N^2)가 되지는 않는다.
for i in range(n-1):
    dist_sum = dist[i]
    # 이미 비용처리를 앞서 했다면 밑의 for 문을 생략
    if visited[i]:  # 시간 복잡도 개선
        continue
    # 시작 도시 바로 다음 도시부터 차례대로 비용 비교
    for j in range(i+1, n):
        # 비용이 뒤에 도시보다 크거나 도시의 끝에 도달하면
        if cost[i] > cost[j] or j == (n-1):
            result += cost[i] * dist_sum
            break  # 반복 종료
        else:
            # 거리를 누적
            dist_sum += dist[j]
            # 비용처리를 했다면 해당 인덱스에 대해 방문한 것으로 친다.
            visited[j] = True

print(result)
