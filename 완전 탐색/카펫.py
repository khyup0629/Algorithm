def solution(brown, yellow):
    answer = []

    j = 0
    for i in range(1, yellow + 1):
        if yellow % i == 0:  # i*j=노란색칸의 갯수
            j = yellow // i  # 소숫점이 나오면 안됨.
        if i >= j:  # (b : 가로 길이) >= (h : 세로 길이)
            b = i
            h = j
        else:
            b = j
            h = i
        if (b + 2) * (h + 2) - (b * h) == brown:  # (b+2)*(h+2)-(b*h)=갈색칸의 갯수
            answer = [b + 2, h + 2]
            return answer

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42842#
