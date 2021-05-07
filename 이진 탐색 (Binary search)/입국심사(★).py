# start, end값 설정에 신경써야한다.

def solution(n, times):
    answer = 0

    start, end = 1, int(1e18)  # end값 설정을 잘해야 한다.
    # 기다리는 사람이 10억명, 심사관이 1명일 때, 심사시간이 10억분이라면, 1e18분이 최댓값이 된다.
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in times:
            cnt += (mid // i)
        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/43238#
