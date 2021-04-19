# 같은 위치에 있을 때를 간과했다
# BFS 를 이용. 핵심 아이디어는 트리 구조를 통해서 같은 층에 있는 탐색 노드들은
# 모두 묶어서 큐에 저장한다.
# 현재 위치가 k보다 크게 되면 -1 밖에 경우의 수가 없으니
# 따로 제한 설정을 통해 계산 시간과 메모리를 줄일 수 있다.

from collections import deque

n, k = map(int, input().split(' '))
# 최대 입력값이 100,000이므로, 2배를 고려하는 경우의 수까지 생각해
# 최대 200,000칸으로 잡는다.
visited = [False] * 200000


def bfs(x):
    q = deque()
    q.append([x])
    visited[x] = True
    cnt = 0
    # 같은 위치에 있을 때는 0을 반환하고 함수 종료
    if x == k:
        return cnt
    while True:
        z = q.popleft()
        # 같은 cnt 의 노드들을 모두 묶어서 큐에 저장하기 위한 임시 저장소
        temp_data = []
        for a in z:
            # 계산 과정과 메모리를 줄이기 위한 조건
            # 현재 위치가 k보다 큰 경우는 무조건 -1만을 탐색하도록
            if a > k:
                nx = a - 1
                # 도착 위치에 도착하면 카운트 +1 해준 뒤 바로 cnt 반환 후 종료
                if nx == k:
                    cnt += 1
                    return cnt
                # 최대로 고려할 수 있는 경우 중 최대값인 200,000 내로 들 경우
                if 0 <= nx < 200000:
                    if not visited[nx]:
                        visited[nx] = True
                        temp_data.append(nx)
            else:
                # -1, +1, *2 탐색
                for i in range(3):
                    # X-1, X+1, 2X
                    dx = [-1, 1, a]
                    nx = a + dx[i]
                    if nx == k:
                        cnt += 1
                        return cnt
                    if 0 <= nx < 200000:
                        if not visited[nx]:
                            visited[nx] = True
                            temp_data.append(nx)
        # 같은 cnt 에서 탐색된 모든 노드들을 묶어서 큐에 저장
        q.append(temp_data)
        cnt += 1


print(bfs(n))

"""
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
"""