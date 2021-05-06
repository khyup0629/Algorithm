# combinations를 쓰지 않고 조합의 경우를 구하는 방법이 있었다.
# 각 종류에서 한 개씩 뽑아서(안 뽑을 수도 있음) 조합의 경우의 수를 구한다면
# 각 종류에 들어있는 개수를 +1해서 모두 곱한 뒤 마지막 값에서 -1을 하면 된다.

def solution(clothes):
    cnt = {}
    for a, b in clothes:  # 종류별 개수를 기록한다.
        cnt[b] = cnt.get(b, 0) + 1

    answer = 1
    for i in cnt:  # (각 종류의 원소의 개수+1)를 모두 곱해준다.
        answer *= (cnt[i] + 1)

    return answer - 1  # 마지막에 -1을 해준다.

# 정확도 96.4점(기존 풀이)
# combinations를 이용할 경우 시간 초과
# combinations는 개수가 8 이상이면 사용하지 말 것.
from itertools import combinations

# 초기 딕셔너리의 value를 list형으로 설정.
# kind = defaultdict(list)
# cnt = defaultdict(int)


def solution(clothes):
    answer = 0

    cnt = {}
    for a, b in clothes:
        cnt[b] = cnt.get(b, 0) + 1

    for i in cnt:
        answer += cnt[i]

    for i in range(2, len(cnt) + 1):
        combi = list(combinations(cnt, i))
        for j in combi:
            multi = 1
            for k in j:
                multi *= cnt[k]
            answer += multi

    return answer