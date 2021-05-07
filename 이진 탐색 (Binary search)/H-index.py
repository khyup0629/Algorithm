# 이진 탐색을 이용해서 계산 시간을 확연히 줄일 수 있다.

from bisect import bisect_left


def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()  # 정렬시켜서 이진 탐색

    end = citations[-1]
    for h in range(end + 1):  # 인용 횟수
        index = bisect_left(citations, h)  # 이진 탐색
        cit = n - index  # h번 이상 인용된 논문 갯수
        rest = index - 0  # 나머지 논문 갯수
        if cit >= h and rest <= h:
            answer = max(answer, h)

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42747#
