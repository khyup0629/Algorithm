# 정확성 33.3(100%), 효율성 31.3으로 총 64.4점을 받은 문제.
# 딕셔너리의 지우는 기능을 몰랐기에 효율성을 줄일 수 없었다.
# del 이라는 함수를 알고나니 딕셔너리의 길이 비교를 통해
# 바로 효율성 100%를 받을 수 있었다.

def solution(gems):
    # 배열의 모든 종류의 보석
    jew_set = list(set(gems))
    n = len(gems)
    jew = {}
    end = 0
    cnt = 1
    temp = n + 2  # 최대로 나올 수 있는 길이 n + 1에서 +1
    for start in range(n):
        while len(jew) < len(jew_set) and end < n:
            jew[gems[end]] = jew.get(gems[end], 0) + 1
            end += 1
        if len(jew) == len(jew_set):
            cnt = end - start
            if cnt < temp:
                temp = cnt
                result_start = start + 1
                result_end = end
        jew[gems[start]] -= 1
        if jew[gems[start]] == 0:
            del jew[gems[start]]

    answer = [result_start, result_end]
    return answer

# 문제 풀이
# https://programmers.co.kr/learn/courses/30/lessons/67258#
