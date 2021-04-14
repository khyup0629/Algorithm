# (주의) 1개로 존재하는 요소들도 모두 개수로 쳐야 한다
# PyPy3 해결

import sys
sys.setrecursionlimit(100000)
# 재귀 제한 해제


def dfs(x):
    # count 를 넣어서 기존에 pair[x]내의 모든 노드들이
    # 이미 방문완료가 되어서 for 문을 그냥 나오는 경우 연결 요소 개수로 세지 않는다.
    global count
    # 1개로 존재하는 요소들도 개수로 치기 위해 pair[x]가 비어있는 경우 1 반환
    if not pair[x]:
        return 1
    for k in pair[x]:
        if visited[k] == 0:
            visited[k] = 1
            dfs(k)
            count = 1
    return count


n, m = map(int, input().split(' '))

# 방문 여부 리스트 생성
visited = [0 for _ in range(n+1)]

# 간선 정리
pair = [[] for _ in range(n+1)]
for i in range(m):
    start, end = map(int, input().split(' '))
    pair[start].append(end)
    pair[end].append(start)


result = 0
for i in range(1, n+1):
    count = 0
    visited[i] = 1
    if dfs(i) == 1:
        result += 1

print(result)

"""
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
예제 입력 2 
6 3
2 1
2 3
5 6
예제 출력 2
3
"""