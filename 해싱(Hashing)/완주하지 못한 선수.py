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
