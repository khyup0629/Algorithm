# 정확성 정답, 효율성 오답

def solution(info, query):
    answer = []

    for i in query:
        cnt = 0
        temp = i.split(' ')
        for j in info:
            temp_info = j.split(' ')
            if temp[0] == temp_info[0] and temp[2] == temp_info[1] and temp[4] == temp_info[2] and \
                    temp[6] == temp_info[3] and int(temp[7]) <= int(temp_info[4]):
                cnt += 1
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150",
        "cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))
