def dfs(x, y):
    # global 을 통해 count 를 가져와서 활용 가능
    global count
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        # 상하좌우 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = 0
result_count = []
for i in range(N):
    for j in range(N):
        # 1에서 0으로 바뀌는 것에 대한 개수를 카운트
        count = 0
        if dfs(i, j):
            result_count.append(count)
            result += 1

print(result)

result_count.sort()
for i in result_count:
    print(i)

"""
입력 예시1
5
11010
10010
01001
11101
10011

출력 예시1
4
2
3
4
5

입력 예시2
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

출력 예시2
3
7
8
9
"""