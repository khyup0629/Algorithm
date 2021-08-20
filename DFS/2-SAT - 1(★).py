# 문제 풀이 아이디어
# 1. n의 개수만큼 True, False를 가지는 모든 경우의 수를 고려합니다.
# (n의 범위가 20이하이므로, 최대 2^20 = 약 1,000,000의 경우의 수를 가집니다)
# 2. exit()를 이용해 CNF식이 true의 경우를 발견했을 경우 바로 실행이 종료되도록 합니다.

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m = map(int, input().split())

cnf = []
for _ in range(m):
    i, j = map(int, input().split())
    cnf.append([i, j])


def dfs(word):  # n의 개수만큼 경우의 수를 하나씩 만들기
    if len(word) == n+1:  # 1번 인덱스부터 n개의 값이 생성되었다면,
        sat(word)  # CNF -> True or False를 판별
        return
    for i in range(2):
        dfs(word+[i])


def sat(word):  # CNF -> True or False를 판별
    for xi, xj in cnf:  # '절'을 하나씩 탐색합니다.
        jul1 = word[xi] if xi > 0 else not word[-xi]
        jul2 = word[xj] if xj > 0 else not word[-xj]
        if (jul1 or jul2) == 0:  # '절'중 하나라도 False이면 CNF는 True가 아닙니다.
            return
    # 위의 for문을 거쳤다는 것은 '절'들이 모두 True라는 뜻입니다.
    # 따라서, 1을 출력하고 실행을 종료합니다.
    print(1)
    exit()


dfs([''])  # 인덱스를 맞춰주기 위한 빈 문자열
# CNF가 True가 되는 경우가 없다면 정상적으로 dfs가 종료됩니다. 그러므로 0을 출력합니다.
print(0)

# 문제 : https://www.acmicpc.net/problem/11277
