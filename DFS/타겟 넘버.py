import sys

sys.setrecursionlimit(10 ** 6)

answer = 0  # target == result의 갯수


def solution(numbers, target):
    result = 0  # 덧셈, 뺄셈의 결과값
    dx = ['+', '-']
    n = len(numbers)

    def dfs(x, result):
        global answer
        if x == n:
            if result == target:
                answer += 1
                return
            return
        for i in range(2):
            if dx[i] == '+':
                result += numbers[x]
                dfs(x + 1, result)
                result -= numbers[x]  # 백트래킹
            else:
                result -= numbers[x]
                dfs(x + 1, result)
                result += numbers[x]  # 백트래킹

    dfs(0, result)

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/43165#
