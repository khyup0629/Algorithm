'''

N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

입력 조건
- 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1 <= N,M <= 1,000)
- 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어집니다.
- 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
출력 조건
- 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.

입력 예시
4 5
00110
00011
11111
00000

출력 예시
3

'''


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    # 1은 방문 완료, 0은 미 방문
    if frame[x][y] == 0:
        # 해당 노드 방문 처리
        frame[x][y] = 1
        # 인접해있는 0을 모두 방문인 1로 만듦
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


N, M = map(int, input().split(' '))

frame = []
for i in range(N):
    # list(map(int, 문자열)) : 문자열을 숫자로 만든 후 리스트화
    frame.append(list(map(int, input())))

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)
