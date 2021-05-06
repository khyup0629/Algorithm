# 개선된 코드
# 정렬과 관련된 코드들을 한 줄로 압축할 수 있었다.
from collections import defaultdict


def solution(genres, plays):
    answer = []
    n = len(genres)

    # "장르" : 총 재생횟수
    genres_sum = {}
    # "장르" : [(현재 노래의 재생횟수, 현재 노래 고유 번호)]
    plays_priority = defaultdict(list)
    for i in range(n):
        genres_sum[genres[i]] = genres_sum.get(genres[i], 0) + plays[i]
        # (현재 노래의 재생횟수, 현재 노래 고유 번호)
        plays_priority[genres[i]].append((plays[i], i))

    # {"장르" : 총 재생횟수}가 저장된 genres_sum 딕셔너리의 key값을 value에 따라 내림차순 정렬.
    genres_priority = sorted(genres_sum.keys(), key=lambda x: genres_sum[x], reverse=True)

    for b in genres_priority:
        # 장르 내 노래의 재생횟수 별로 내림차순 정렬(-x[0])
        # '-'를 이용해 내림차순 정렬 구현 가능
        # 추가할 두 노래의 재생횟수가 같은 경우 인덱스가 작은 것을 먼저 출력(x[1])
        plays_priority[b].sort(key=lambda x: (-x[0], x[1]))
        if len(plays_priority[b]) != 1:  # 장르에 속한 곡이 1곡이 아닐 경우,
            answer.append(plays_priority[b][0][1])
            answer.append(plays_priority[b][1][1])
        else:  # 장르에 속한 곡이 1곡일 경우 1곡만 추가
            answer.append(plays_priority[b][0][1])

    return answer

# 개선 전 코드
from collections import defaultdict


def solution(genres, plays):
    answer = []
    n = len(genres)

    # "장르" : 총 재생횟수
    genres_sum = {}
    # "장르" : [(현재 노래의 재생횟수, 현재 노래 고유 번호)]
    plays_priority = defaultdict(list)
    for i in range(n):
        genres_sum[genres[i]] = genres_sum.get(genres[i], 0) + plays[i]
        # (현재 노래의 재생횟수, 현재 노래 고유 번호)
        plays_priority[genres[i]].append((plays[i], i))

    # 자료 구조 : (총 재생횟수, 장르) 저장
    genres_priority = []
    for i in genres_sum:
        # (총 재생횟수, 장르)
        genres_priority.append((genres_sum[i], i))
    # 총 재생횟수 순서로 내림차순 정렬
    genres_priority.sort(reverse=True)

    # 장르 내 노래의 재생횟수 별로 내림차순 정렬
    for i in plays_priority:
        plays_priority[i].sort(reverse=True)

    for a, b in genres_priority:
        if len(plays_priority[b]) != 1:  # 장르에 속한 곡이 1곡이 아닐 경우,
            # 추가할 두 노래의 재생횟수가 같은 경우
            if plays_priority[b][0][0] == plays_priority[b][1][0]:
                # 인덱스가 작은 것을 먼저 출력
                if plays_priority[b][0][1] < plays_priority[b][1][1]:
                    answer.append(plays_priority[b][0][1])
                    answer.append(plays_priority[b][1][1])
                else:
                    answer.append(plays_priority[b][1][1])
                    answer.append(plays_priority[b][0][1])
            # 추가할 두 노래의 재생횟수가 같지 않으면, 앞에서부터 순서대로 추가
            else:
                answer.append(plays_priority[b][0][1])
                answer.append(plays_priority[b][1][1])
        else:  # 장르에 속한 곡이 1곡일 경우 1곡만 추가
            answer.append(plays_priority[b][0][1])

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42579
