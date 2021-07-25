# 문제 풀이 아이디어
# 1. *로 이루어진 n x n 행렬을 만든다.
# 2. 3 x 3이 될 때까지 분할하며 가운데 부분의 *을 빈 칸으로 만든다.
import sys
sys.setrecursionlimit(10**5)
n = int(input())
graph = [['*'] * n for _ in range(n)]  # 초기에 *로 이루어진 n x n 행렬을 만든다.


def divide_conquer(point, standard):
    for x, y in point:
        if standard != 3:  # 3 x 3이 될 때까지 분할
            point = [(x, y), (x, y + standard // 3), (x, y + 2 * standard // 3),
                     (x + standard // 3, y), (x + standard // 3, y + standard // 3),
                     (x + standard // 3, y + 2 * standard // 3),
                     (x + 2 * standard // 3, y), (x + 2 * standard // 3, y + standard // 3),
                     (x + 2 * standard // 3, y + 2 * standard // 3)]
            divide_conquer(point, standard // 3)
        standard_empty = standard // 3
        # 가운데 부분에 해당하는 곳의 *을 빈 칸으로 만든다.
        for i in range(x + standard_empty, x + standard_empty + standard_empty):
            for j in range(y + standard_empty, y + standard_empty + standard_empty):
                graph[i][j] = ' '


point = [(0, 0)]
divide_conquer(point, n)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end='')
    print()

# 문제 : https://www.acmicpc.net/problem/2447
