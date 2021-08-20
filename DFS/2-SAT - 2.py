# 2-SAT - 1 문제와 거의 같은 문제이다.
import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

cnf = []
for _ in range(m):
    i, j = map(int, input().split())
    cnf.append([i, j])


def dfs(word):
    if len(word) == n + 1:
        sat(word)
        return
    for a in range(2):
        dfs(word+[a])


def sat(word):
    for xi, xj in cnf:
        element_1 = word[xi] if xi > 0 else not word[-xi]
        element_2 = word[xj] if xj > 0 else not word[-xj]
        if (element_1 or element_2) == 0:
            return
    print(1)
    for i in range(1, n+1):
        print(word[i], end=' ')
    exit()


dfs([])
print(0)

# 문제 : https://www.acmicpc.net/problem/11278
