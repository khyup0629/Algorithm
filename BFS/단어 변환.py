# 단어가 하나만 다른 것을 q에 추가해가며 BFS로 해결하면 된다.

from collections import deque


def solution(begin, target, words):
    answer = 0

    if target not in words:  # words에 target 단어가 없다면 target으로 변환 불가능.
        return 0

    visited = {}  # 문자열을 인덱스로 하기 위해 딕셔너리 이용

    q = deque()
    q.append([begin])
    cnt = 0
    while True:
        now = q.popleft()
        temp = []  # 한 번에 묶어서 처리하기 위함.
        cnt += 1  # begin과 target이 같은 경우가 없기 때문에 식을 이 위치에 써도 무방.
        for x in now:
            visited[x] = True
            for i in words:
                if not visited.get(i):
                    dif = 0
                    for a, b in zip(x, i):  # 다른 글자가 몇 개 있는지
                        if a != b:
                            dif += 1
                    if dif == 1:  # 다른 글자가 1개라면,
                        temp.append(i)
                        if i == target:  # target에 도착했다면 카운트 return.
                            return cnt
        if not temp:  # 중간에 끊겨서 아무곳도 갈 수 없는 경우
            return 0  # target으로 변환 불가능
        q.append(temp)

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/43163#
