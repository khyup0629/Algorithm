# 문제 풀이 아이디어
# 1. 퍼즐을 한 칸씩 탐색하며 아래를 수행한다.
# 2. ↑ 가 막혀 있고, ↓가 뚫려 있는 칸 선정
#    현재 칸으로부터 아래로 끝까지 내려가면서 '#'가 나올 때까지 알파벳을 추가한다.
# 3. ← 가 막혀 있고, →가 뚫려 있는 칸 선정
#    현재 칸으로부터 오른쪽으로 끝까지 가면서 '#'가 나올때 까지 알파벳을 추가한다.
# 4. 막혀있다의 기준은 퍼즐의 범위를 벗어나거나 '#'을 마주했을 때이다.
r, c = map(int, input().split())

graph = []
for _ in range(r):
    arr = input()
    graph.append(arr)


def able_word_down(x, y):  # ↑ 가 막혀 있고, ↓가 뚫려 있는 칸 선정
    global result
    nx_u, ny_u = x - 1, y  # 위쪽
    nx_d, ny_d = x + 1, y  # 아래쪽
    if nx_u < 0 or graph[nx_u][ny_u] == '#':  # 위쪽이 막혀있다면,
        if 0 <= nx_d < r and graph[nx_d][ny_d] != '#':  # 아래쪽이 뚫려 있다면,
            # 현재 칸으로부터 아래로 끝까지 내려가면서 '#'가 나올 때까지 알파벳을 추가한다.
            ans = ''
            for i in range(x, r):
                if graph[i][y] == '#':
                    break
                ans += graph[i][y]  # 단어 알파벳을 하나씩 추가
            result.append(ans)  # 단어를 result에 추가


def able_word_right(x, y):  # ← 가 막혀 있고, →가 뚫려 있는 칸 선정
    global result
    nx_l, ny_l = x, y - 1  # 왼쪽
    nx_r, ny_r = x, y + 1  # 오른쪽
    if ny_l < 0 or graph[nx_l][ny_l] == '#':  # 왼쪽으로 막혀있다면,
        if 0 <= ny_r < c and graph[nx_r][ny_r] != '#':  # 오른쪽으로 뚫려있다면,
            # 현재 칸으로부터 오른쪽으로 끝까지 가면서 '#'가 나올때 까지 알파벳을 추가한다.
            ans = ''
            for j in range(y, c):
                if graph[x][j] == '#':
                    break
                ans += graph[x][j]
            result.append(ans)


result = []
for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':  # '#' 칸이 아닌 곳에서 함수 수행
            able_word_down(i, j)
            able_word_right(i, j)

print(sorted(result)[0])  # 오름차순 정렬의 첫 번째 원소 출력
