# 좀 무식하게 코드를 쓴 감이 있는데, 내겐 가장 최선의 방법이었다.
# 문제 풀이 아이디어
# 1. 재귀 함수를 이용해 DFS로 cctv의 개수만큼 들어간다.
# 2. cctv의 개수(리프 노드)에 도달하기까지 (감시방향, x좌표, y좌표)를 t_case에 저장한다.
# 3. cctv의 개수(리프 노드)에 도달하면, 감시방향과 위치 정보를 바탕으로 감시되는 빈 칸을 '#'로 바꾼다.
# 4. 남아있는 0의 개수를 세고, 그 중 최솟값을 구한다.
# 5. .pop()을 이용해 백트래킹을 한다.
import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())

t_graph = []  # 초기 지도
for _ in range(n):
    arr = list(map(int, input().split()))
    t_graph.append(arr)

cctv_pos = []  # cctv의 위치와 그 위치에서 감시해야하는 방향이 튜플 형태로 저장된다.
cctv_cnt = 0  # cctv의 개수, 재귀 함수의 return 조건으로 사용된다.
for i in range(n):
    for j in range(m):
        if 1 <= t_graph[i][j] <= 5:
            cctv_pos.append((t_graph[i][j], i, j))
            cctv_cnt += 1
t_case = []  # (상하좌우, x좌표, y좌표) : cctv의 위치와 그 위치에서 감시해야하는 방향이 저장될 저장소
cctv_pos += [(0, 0, 0)]  # 재귀 함수에 인덱스 에러가 발생하게 하지 않기 위함.


def cctv(num, x, y, cnt):
    global _min
    # DFS 탐색으로 리프 노드까지 들어왔다면,
    # t_case에 저장된 감시 방향과 위치 정보를 이용해서 감시 가능한 영역을 '#'로 만든다.
    if cnt > cctv_cnt:
        # 지도 초기화
        graph = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                graph[i][j] = t_graph[i][j]
        # t_case에 저장된 감시 방향과 위치 정보를 이용해서 감시 가능한 영역을 '#'로 만든다.
        for direc, x, y in t_case:
            if direc == 0:  # 상
                for i in range(x - 1, -1, -1):
                    if graph[i][y] == 6:  # 벽을 마주치면 반복 종료
                        break
                    graph[i][y] = '#'
            elif direc == 1:  # 하
                for i in range(x + 1, n):
                    if graph[i][y] == 6:
                        break
                    graph[i][y] = '#'
            elif direc == 2:  # 좌
                for j in range(y - 1, -1, -1):
                    if graph[x][j] == 6:
                        break
                    graph[x][j] = '#'
            else:  # 우
                for j in range(y + 1, m):
                    if graph[x][j] == 6:
                        break
                    graph[x][j] = '#'
        # 지도에 남아있는 0의 개수를 세고 그 중 최솟값을 찾는다.
        cnt_0 = 0  # 지도의 남아있는 0의 개수
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    cnt_0 += 1
        _min = min(_min, cnt_0)
        return
    # cctv의 종류에 따라 가능한 경우의 수 고려.
    # (상하좌우, x, y) : 상(0), 하(1), 좌(2), 우(3)
    if num == 1:  # 1번 cctv는 총 4가지의 경우의 수
        for i in range(4):
            t_case.append((i, x, y))
            cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt+1)
            t_case.pop()  # 백트래킹
    elif num == 2:  # 2번 cctv는 총 2가지의 경우의 수
        t_case.append((0, x, y))
        t_case.append((1, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.append((2, x, y))
        t_case.append((3, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
    elif num == 3:  # 3번 cctv는 총 4가지의 경우의 수
        t_case.append((0, x, y))
        t_case.append((3, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.append((3, x, y))
        t_case.append((1, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.append((1, x, y))
        t_case.append((2, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.append((2, x, y))
        t_case.append((0, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
    elif num == 4:  # 4번 cctv는 총 4가지의 경우의 수
        t_case.append((0, x, y))
        t_case.append((1, x, y))
        t_case.append((2, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.pop()
        t_case.append((0, x, y))
        t_case.append((1, x, y))
        t_case.append((3, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.pop()
        t_case.append((2, x, y))
        t_case.append((3, x, y))
        t_case.append((0, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.pop()
        t_case.append((2, x, y))
        t_case.append((3, x, y))
        t_case.append((1, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.pop()
    else:  # 5번 cctv는 1가지의 경우의 수
        t_case.append((0, x, y))
        t_case.append((1, x, y))
        t_case.append((2, x, y))
        t_case.append((3, x, y))
        cctv(cctv_pos[cnt][0], cctv_pos[cnt][1], cctv_pos[cnt][2], cnt + 1)
        t_case.pop()
        t_case.pop()
        t_case.pop()
        t_case.pop()


_min = int(1e9)
cctv(cctv_pos[0][0], cctv_pos[0][1], cctv_pos[0][2], 1)

print(_min)

# 문제 : https://www.acmicpc.net/problem/15683
