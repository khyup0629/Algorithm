# 다익스트라 알고리즘을 베이스로 문제를 풀면 된다.
# 1. 비용이 작은 것부터 고려해주기 위해 힙 자료구조를 이용한다.
# 2. 최대 입력값의 2배를 저장 공간으로 둔다.
# 3. 비용의 경우가 3가지가 있다(0, 1, 1). 비용이 작은 것부터 고려한다.
#   (입력이 1 2일 경우 비용 순으로 경우를 고려해야 최초로 k 위치에 도달했을 때 최소 비용으로 출력할 수 있다.)

import heapq

n, k = map(int, input().split())
INF = int(1e9)

dist = [INF] * 200000


def dijkstra(n):
    if n == k:  # 둘이 같을 경우 이동할 필요가 없다.
        print(0)
        return
    q = []
    heapq.heappush(q, (0, n))
    dist[n] = 0
    while True:
        # print(q)
        # print 함수가 있는 경우 계산 속도가 느려질 수 밖에 없다.
        # 계산시간을 체크하고 싶을 때는 꼭 print 없이 실행하도록 하자.
        distance, now = heapq.heappop(q)
        # 다른 곳을 거쳐서 현재 위치로 다시 올 수도 있는데
        # 지금까지 알려진 현재 위치의 최소 비용보다 클 경우는 밑의 코드를 고려할 필요가 없다.
        if dist[now] < distance:
            continue
        if now > k:  # 현재 위치가 k보다 클 경우 -1만 해주면 된다.
            nx = now - 1
            cost = distance + 1
            if dist[nx] > cost:
                # 비용이 작은 순으로 q에 들어가기 때문에
                # 최초로 nx == k가 나오는 순간이 최소 비용이 된다.
                if nx == k:
                    print(cost)
                    return
                dist[nx] = cost
                heapq.heappush(q, (cost, nx))
        else:
            dx = [now, -1, 1]  # 비용이 작은 순으로 비교
            dcost = [0, 1, 1]  # 1 2일 경우 -1, 1, 0순으로 하면 답이 1이 나온다.
            for i in range(3):
                nx = now + dx[i]
                cost = distance + dcost[i]
                if 0 <= nx < 200000 and dist[nx] > cost:
                    if nx == k:
                        print(cost)
                        return
                    dist[nx] = cost
                    heapq.heappush(q, (cost, nx))


dijkstra(n)

# 문제 : https://www.acmicpc.net/problem/13549
