import heapq


def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:  # 1,000,000
        heapq.heappush(q, i)

    while True:
        a = heapq.heappop(q)
        if a >= K:
            return answer
        if not q:
            return -1
        b = heapq.heappop(q)
        soc = a + b * 2
        heapq.heappush(q, soc)
        answer += 1

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42626#
