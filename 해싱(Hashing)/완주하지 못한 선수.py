# 계산 시간이 더 빠른 코드
# 밑에 코드와 비교하면, 이 코드는 participant에 있는 사람이
# completion에 없다면 바로 즉시 값을 반환하고 코드를 종료한다.
def solution(participant, completion):
    answer = ''
    hash_map = {}
    # 같은 키(key)가 들어가면 덮어씌워진다. 그래서 value를 개수로 했다.
    for person in completion:
        hash_map[person] = hash_map.get(person, 0) + 1

    for person in participant:
        if person in hash_map:
            hash_map[person] -= 1
            if hash_map[person] == 0:
                del hash_map[person]
        else:
            return person

    return answer


# a.keys() 에 대해서 알 수 있었던 문제
def solution(participant, completion):
    dic = {}
    for person in participant:
        dic[person] = dic.get(person, 0) + 1

    for person in completion:
        dic[person] -= 1
        if dic[person] == 0:
            del dic[person]
    # a.keys() : dic 딕셔너리의 key 값들을 dict_keys(['leo'])와 같은 형태로 반환한다.
    # list(a.keys()) 로 묶어주면 리스트로 반환된다.
    result = list(dic.keys())
    answer = result[0]
    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42576
