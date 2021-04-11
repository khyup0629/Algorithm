import sys
sys.setrecursionlimit(100000)
# 재귀 제한 해제


def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x - 1, y + 1)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
        return True
    return False


result_count = []
while True:
    w, h = map(int, input().split(' '))

    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split(' '))))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                result += 1

    result_count.append(result)

for i in result_count:
    print(i)

"""
입력 예시
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
출력 예시
0
1
1
3
1
9
"""