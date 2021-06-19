# 모든 로프를 사용할 필요가 없으므로
# 1. 로프를 무게 순으로 오름차순 정렬.
# 2. 제일 무게가 낮은 로프의 무게 * 로프의 개수를 썼던 무게를 제외하면서 최댓값을 계산.
n = int(input())

lope = [int(input()) for _ in range(n)]
lope.sort()

j = len(lope)  # 로프의 개수

_max = 0
# 가장 무게가 작은 로프부터 탐색
for i in range(n):
    w = lope[i] * j  # 현재 가장 무게가 작은 로프 * 현재 로프의 개수
    _max = max(_max, w)
    j -= 1

print(_max)

# 문제 : https://www.acmicpc.net/problem/2217

"""
예제 입력 2
3
10
15
5
예제 출력 2
20
"""