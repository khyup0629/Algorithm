def solution(array, commands):
    answer = []

    for i, j, k in commands:
        result = sorted(array[i - 1:j])
        answer.append(result[k - 1])

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42748
