# 최단 거리를 구하는데 음수 순환이 존재할 가능성도 있기 때문에
# 벨만 포드 최단 거리 알고리즘 이용

import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정


def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    # 전체 n번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(m):
            # 현재 도시
            cur = edges[j][0]
            # 도착 도시
            next_node = edges[j][1]
            # 걸리는 시간
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                # 최단 거리 갱신
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                # 계속 최단 거리가 작아지고 있다는 뜻
                if i == n - 1:
                    return True
    return False


# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    # 시작 도시, 도착 도시, 걸리는 시간
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)

# 음수 순환이 발생할 경우
if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우, -1을 출력
        if dist[i] == INF:
            print("-1")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(dist[i])

"""
예제 입력 1 
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
예제 출력 1 
4
3
예제 입력 2 
3 4
1 2 4
1 3 3
2 3 -4
3 1 -2
예제 출력 2 
-1
예제 입력 3 
4 3
1 2 4
1 2 3
2 4 1
예제 출력 3 
3
-1
4
"""