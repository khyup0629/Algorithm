def solution(answers):
    answer = []
    n = len(answers)
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    # 1번 수포자
    index = 0
    for i in range(n):
        if i % 5 == 0:
            index = 0
        else:
            index += 1
        if answers[i] == num_1[index]:
            cnt_1 += 1
    result.append(cnt_1)
    # 2번 수포자
    index = 0
    for i in range(n):
        if i % 8 == 0:
            index = 0
        else:
            index += 1
        if answers[i] == num_2[index]:
            cnt_2 += 1
    result.append(cnt_2)
    # 3번 수포자
    index = 0
    for i in range(n):
        if i % 10 == 0:
            index = 0
        else:
            index += 1
        if answers[i] == num_3[index]:
            cnt_3 += 1
    result.append(cnt_3)
    # 1번부터 3번까지 차례대로 최댓값과 같은 인덱스를 기록.(자연히 오름차순으로 기록됨.)
    _max = max(result)
    for i in range(3):
        if result[i] == _max:
            answer.append(i + 1)

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42840#
