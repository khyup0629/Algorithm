# 전형적인 BFS 문제
# bfs 함수의 return 값을 분리된 칸의 개수로 출력한다.

from collections import deque
# m : 세로 길이, n : 가로 길이, k : 직사각형 개수
m, n, k = map(int, input().split(' '))
# 방문/미방문 여부, 0 : 빈 칸, 1 : 직사각형
frame = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    start_x, start_y, end_x, end_y = map(int, input().split(' '))
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            frame[i][j] = 1
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    frame[x][y] = 1
    # bfs 함수의 return 값으로 빈 칸의 개수를 반환하기 위함
    cnt = 1
    # q가 비어있으면 종료.
    while q:
        x, y = q.popleft()
        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if frame[nx][ny] == 0:
                    # 아직 미방문한 곳이라면 방문처리 후 빈 칸 개수 +1
                    frame[nx][ny] = 1
                    cnt += 1
                    q.append((nx, ny))
    return cnt


result = 0
count = []
for i in range(n):
    for j in range(m):
        if frame[i][j] == 0:
            # bfs 함수를 거치면서 최초 0인 지점부터 연결된 모든 0이
            # 1로 바뀔 것이므로 최초로 0이 되는 부분일 때 result += 1 을 해주면
            # 영역의 개수를 구할 수 있다.
            result += 1
            count.append(bfs(i, j))
# 빈 칸의 개수를 오름차순 정렬 후 출력
count.sort()
print(result)
print(' '.join(map(str, count)))

"""
문제
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때,
이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 
그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.

<그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.
M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, 
K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 
그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 
둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 
차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 
입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

예제 입력 1 
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
예제 출력 1 
3
1 7 13
"""
