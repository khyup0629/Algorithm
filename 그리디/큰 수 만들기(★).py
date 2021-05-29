# 고민 끝에 우선순위 큐를 사용해 풀었다.
# 문제 풀이 아이디어
# 1. 제거할 개수 k + 1만큼 number 에서 우선순위 큐에 넣는다.
# 우선순위 큐에 넣을 때 형식은 (-숫자, 인덱스)
# 2. 우선순위 큐의 첫 번째 값의 '인덱스' 가 standard 보다 작으면 반복을 스킵한다.
# 3. 아니라면 standard 를 현재 '인덱스' 로 갱신, answer 에 '숫자' 를 추가,
# 남은 숫자의 개수를 뜻하는 n_ans 를 -1, k를 +1
# 4. 우선순위 큐에 새로운 k 값에 대응하는 (-숫자, 인덱스)를 추가한다.
# 5. 남은 숫자의 개수가 0이 되면 반복을 종료한다.

import heapq


def solution(number, k):
    answer = ''
    number = list(number)
    n = len(number)
    n_ans = n - k  # 남은 숫자의 개수
    q = []  # 우선순위 큐
    for i in range(k + 1):
        heapq.heappush(q, (-int(number[i]), i))

    standard = -1
    while n_ans != 0:
        num, idx = heapq.heappop(q)
        if idx < standard:  # 기준 인덱스의 앞에 위치하면 안된다.
            continue
        standard = idx
        answer += str(-num)
        n_ans -= 1
        k += 1
        if k == n:  # 우선순위 큐에 추가할 때 범위를 벗어나는 것을 막는 역할.
            continue
        heapq.heappush(q, (-int(number[k]), k))

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42883#

# (시행 착오)여전히 시간 초과지만 약 2배 정도 빠르기가 개선된 코드


def solution(number, k):
    answer = ''
    number = list(number)
    n = len(number)
    n_ans = n - k

    start, end = -1, k
    while n_ans != 0:
        _max, m_index = -1, 0
        for i in range(start + 1, end + 1):
            if _max < int(number[i]):
                _max = int(number[i])
                m_index = i
        answer += str(_max)
        start = m_index
        end += 1
        n_ans -= 1
        # print(start, end)

    return answer

# (시행 착오)시간 초과


def solution(number, k):
    answer = ''
    number = list(number)
    n = len(number)
    n_ans = n - k
    arr = []
    for i in range(n):
        arr.append((int(number[i]), i))

    arr.sort(key=lambda x: (-x[0], x[1]))
    # print(arr)

    standard_index = -1
    while n_ans != 0:
        for value, index in arr:
            if n - index < n_ans or index <= standard_index:
                continue
            answer += str(value)
            n_ans -= 1
            standard_index = index
            break

    return answer
