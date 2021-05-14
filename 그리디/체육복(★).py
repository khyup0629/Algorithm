# 제한사항 : 여벌 체육복을 가진 학생이 도난 당한 경우 자기 자신을 위해 입어야 하므로
# 다른 사람에게 빌려줄 옷이 없게 된다.
# 그래서 reserve에서 제거해야한다.
def solution(n, lost, reserve):
    answer = n - len(lost)

    q = []  # q에는 reserve와 lost에 동시에 속한 원소를 제외한 reserve원소가 들어간다.
    for i in reserve:
        if i in lost:
            answer += 1
            lost.remove(i)
        else:
            q.append(i)

    for i in q:
        if i - 1 in lost:
            answer += 1
            lost.remove(i - 1)
        elif i + 1 in lost:
            answer += 1
            lost.remove(i + 1)
    return answer


# 해시를 이용한 방법
def solution(n, lost, reserve):
    answer = n - len(lost)

    reserve_dic = {}
    for i in reserve:
        reserve_dic[i] = i

    lost_dic = {}
    for i in lost:
        lost_dic[i] = i
        if i in reserve_dic:
            del reserve_dic[i]
            del lost_dic[i]
            answer += 1

    for i in reserve_dic:
        if i - 1 in lost_dic:
            answer += 1
            del lost_dic[i - 1]
        elif i + 1 in lost_dic:
            answer += 1
            del lost_dic[i + 1]

    return answer

# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42862#
