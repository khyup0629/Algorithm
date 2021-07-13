# 문제는 맞게 풀었는데, 사소한 곳에서 쓸데없이 고민했다.
# 2차원 배열의 최대/최소값을 구할 때 단순히 max(max())를 하면 안된다.
# max(map(max, array)) 이렇게 'map' 메서드를 써주어야 한다.
# 입력값의 범위를 고려했을 때 시간 복잡도를 O(N^2)로 완전 탐색해도 시간 안에 해결 가능.
import sys
sys.setrecursionlimit(10**5)
n = int(input())
t_graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    t_graph.append(arr)


def move(k):  # 상, 하, 좌, 우
    visited = [[False] * n for _ in range(n)]
    if k == 0:  # 위로 쏠릴 때
        # 블럭들을 모두 위로 모아준다.
        for j in range(n):
            cnt_0 = 0  # 한 열씩 탐색할 때 그 열의 0의 개수
            for i in range(n):
                if graph[i][j] == 0:  # 빈 칸이라면
                    cnt_0 += 1  # 0개수 +1
                else:  # 블럭이 있다면
                    # 0의 개수만큼 현재 행에서 빼준 값에 현재 블럭 값을 넣고
                    graph[i-cnt_0][j] = graph[i][j]
                    if cnt_0 != 0:  # 현재까지 적어도 빈 칸이 한 칸이라도 있었다면,
                        graph[i][j] = 0  # 현재 블럭을 빈 칸으로 만든다.
        for j in range(n):  # 한 열당 행을 탐색
            # 임시 저장소(temp)의 초기값은 모두 0
            temp = [[0] for _ in range(n)]  # 합쳐진 블럭들과 남겨진 블럭들이 빈 칸을 메꾼 상황이 저장될 임시 저장소
            cnt = 0  # 임시 저장소(temp)의 행을 가리킨다.
            for i in range(n-1):  # 마지막 행 전까지 탐색
                if not visited[i][j]:  # 방문하지 않았다면,
                    visited[i][j] = True  # 방문 처리
                    if graph[i+1][j] == graph[i][j] and graph[i][j] != 0:  # 현재 블럭이 0이 아니면서 다음 블럭과 수가 같다면,
                        temp[cnt][0] = graph[i][j] * 2  # 임시 저장소의 가장 윗칸에 2배의 값 저장
                        visited[i+1][j] = True  # 다음 블럭은 방문 처리를 해주어 해당 블럭을 탐색하지 않도록 한다.
                        cnt += 1  # 임시 저장소의 비어있는 제일 윗칸을 채웠으니 다음 행을 가리키도록 한다.
                    elif graph[i][j] != 0:  # 합쳐지지 않는 블럭이라면,
                        temp[cnt][0] = graph[i][j]  # 임시 저장소의 가장 윗칸에 현재 블럭을 저장.
                        cnt += 1  # 임시 저장소의 비어있는 제일 윗칸을 채웠으니 다음 행을 가리키도록 한다.
            # 제일 마지막 행 처리
            if not visited[n-1][j]:  # 제일 마지막 행이 방문되지 않았다면, 합쳐지지 않았단 의미.
                temp[cnt][0] = graph[n-1][j]  # 그 수 그대로 올라간다.
            for i in range(n):  # 그래프 갱신
                graph[i][j] = temp[i][0]
    # 마찬가지 아이디어로 하(1), 좌(2), 우(3)를 수행한다.
    elif k == 1:  # 하
        for j in range(n):
            cnt_0 = 0
            for i in range(n-1, -1, -1):
                if graph[i][j] == 0:
                    cnt_0 += 1
                else:
                    graph[i + cnt_0][j] = graph[i][j]
                    if cnt_0 != 0:
                        graph[i][j] = 0
        for j in range(n):
            temp = [[0] for _ in range(n)]
            cnt = n-1
            for i in range(n-1, 0, -1):
                if not visited[i][j]:
                    visited[i][j] = True
                    if graph[i-1][j] == graph[i][j] and graph[i][j] != 0:
                        temp[cnt][0] = graph[i][j] * 2
                        visited[i-1][j] = True
                        cnt -= 1
                    elif graph[i][j] != 0:
                        temp[cnt][0] = graph[i][j]
                        cnt -= 1
            if not visited[0][j]:
                temp[cnt][0] = graph[0][j]
            for i in range(n):
                graph[i][j] = temp[i][0]
    elif k == 2:  # 좌
        for i in range(n):
            cnt_0 = 0
            for j in range(n):
                if graph[i][j] == 0:
                    cnt_0 += 1
                else:
                    graph[i][j-cnt_0] = graph[i][j]
                    if cnt_0 != 0:
                        graph[i][j] = 0
        for i in range(n):
            temp = [[0] * n]
            cnt = 0
            for j in range(n-1):
                if not visited[i][j]:
                    visited[i][j] = True
                    if graph[i][j+1] == graph[i][j] and graph[i][j] != 0:
                        temp[0][cnt] = graph[i][j] * 2
                        visited[i][j+1] = True
                        cnt += 1
                    elif graph[i][j] != 0:
                        temp[0][cnt] = graph[i][j]
                        cnt += 1
            if not visited[i][n-1]:
                temp[0][cnt] = graph[i][n-1]
            for j in range(n):
                graph[i][j] = temp[0][j]
    else:  # 우
        for i in range(n):
            cnt_0 = 0
            for j in range(n-1, -1, -1):
                if graph[i][j] == 0:
                    cnt_0 += 1
                else:
                    graph[i][j+cnt_0] = graph[i][j]
                    if cnt_0 != 0:
                        graph[i][j] = 0
        for i in range(n):
            temp = [[0] * n]
            cnt = n-1
            for j in range(n-1, 0, -1):
                if not visited[i][j]:
                    visited[i][j] = True
                    if graph[i][j-1] == graph[i][j] and graph[i][j] != 0:
                        temp[0][cnt] = graph[i][j] * 2
                        visited[i][j-1] = True
                        cnt -= 1
                    elif graph[i][j] != 0:
                        temp[0][cnt] = graph[i][j]
                        cnt -= 1
            if not visited[i][0]:
                temp[0][cnt] = graph[i][0]
            for j in range(n):
                graph[i][j] = temp[0][j]


# DFS 탐색의 모든 경우의 수를 case에 저장한다.
case = []
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    case.append([a, b, c, d, e])

_max = 0
for group in case:  # 각 경우의 수 별로 최댓값을 구한다.
    # 각 경우의 수를 고려할 때, 항상 graph를 초기 상태로 초기화한다.
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            graph[i][j] = t_graph[i][j]
    # 각 경우의 수의 기울임을 차례대로 시행한다.
    for idx in group:
        move(idx)
    # 주의!!! 2차원 배열의 최대/최솟값을 구할 때 반드시 map을 사용할 것
    _max = max(_max, max(map(max, graph)))  # 최댓값을 구한다.
print(_max)

# 문제 : https://www.acmicpc.net/problem/12100
