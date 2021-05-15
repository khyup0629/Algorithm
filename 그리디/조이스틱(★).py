"""
# 고민을 꽤 많이 했는데 제한사항의 문자열이 20으로 짧은 것을 보고,
# 동일한 문자열을 3번 이어 붙여서 이동하는 방법을 생각해보았다.
# 만약 문자열이 BACAAAAZ 라면, 이 문자열을 3번 이어 붙인다.
# BACAAAAZ|BACAAAAZ|BACAAAAZ, 그리고 인덱스를 0부터 앞에서부터 매긴다.
# 01234567|89... , |...     , 중간부터 AAAAAAAA와 비교해 다른 인덱스를 기록한다.
# AAAAAAAA|AAAAAAAA|AAAAAAAA, [0, 8, 16, 2, 10, 18, 7, 15, 23]
# 처음 시작 위치(현재 위치)를 8로 하고 문자를 같게 하기 위해 이동해야 하는 횟수 중 최솟값을 구한다.
# 해시를 이용해 알파벳 대문자의 아스키코드에서 +-26한 숫자를 같이 기록한다.
# (ABCDE...Z를 3번 이어붙인 것과 같다)
# 'A' = [39, 65, 91] ~ 'Z' : [64, 90, 116]
# 8 % 문자열의 길이 == 인덱스 % 문자열의 길이를 만족하는 인덱스를 지운다.
# [0, 8, 16] 이후, 문자가 다른 인덱스를 기록한 리스트를 거리에 따라 오름차순 정렬한다.
# [7, 10, 2, 15, 18, 23], 다음으로 이동해야 하는 인덱스는 7이므로, 현재 위치에서 7까지
# 이동해야하는 횟수만큼 answer에 더해준다. 이후 현재 위치를 7로 갱신한 후
# 인덱스 리스트가 빌 때까지 반복한다.
"""

from collections import defaultdict


def solution(name):
    answer = 0
    n = len(name)

    # 'A' : [39, 65, 91] ~ 'Z' : [64, 90, 116]
    alpha = defaultdict(list)
    for i in range(65, 91):
        alpha[chr(i)].append(i - 26)
        alpha[chr(i)].append(i)
        alpha[chr(i)].append(i + 26)

    string = ''
    case = []
    for i in range(n):
        string += 'A'
        if string[i] != name[i]:
            case.append(i)
            case.append(i + n)
            case.append(i + n + n)

    name = name * 3  # 3번 이어 붙인다.

    pos = n  # 처음 시작 위치

    while True:
        # 이전 혹은 다음 알파벳으로 가는 횟수가 가장 짧은 횟수 만큼 더해준다.
        answer += min(abs(65 - alpha[name[pos]][0]), abs(65 - alpha[name[pos]][1]), abs(65 - alpha[name[pos]][2]))
        case_new = []  # case에서 현재 위치와 관련한 인덱스를 뺀 원소들을 넣는다.
        for index in case:
            if (pos % n) != (index % n):
                case_new.append(index)
        case = case_new  # 다시 case에 넣어준다.
        case.sort(key=lambda x: abs(pos - x))  # 이동해야 하는 거리가 가장 짧은 순으로 정렬.

        if not case:  # case가 비어있다면 반복 종료.
            break
        answer += abs(pos - case[0])  # 이동해야하는 횟수만큼 더해준다.
        pos = case.pop(0)  # 가장 짧은 이동거리를 가진 인덱스를 현재 위치로 한다.

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42860
