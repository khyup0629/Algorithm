# 2021 NEXT TOSS Server Developer #4
# M일 동안 N회 노출이 되었을 때를 일(day)별로 SHOW한 회수를 저장하는 누적합 테이블(daycnt)을 만들어서 
# daycnt[day] - daycnt[day-m] >= n 의 조건을 만족하면 금융 정보를 띄우지 않도록 합니다.
input = "1 2\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nEXIT"
input = "2 3\nSHOW\nNEGATIVE\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW\nEXIT"
input = "1 3\nSHOW\nHELLO\nEXIT"
input = "1 3\nHELLO"
input = "3 7\nSHOW\nSHOW\nNEXT\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nSHOW\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW" \
        "\nNEXT\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nEXIT"
input = "3 7\nSHOW\nSHOW\nNEXT\nSHOW\nNEGATIVE\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nSHOW\nSHOW\nSHOW" \
        "\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nEXIT"

answer = ''
s = input.split('\n')
m = int(s[0][0])
n = int(s[0][2])
answer += str(m) + " " + str(n)

daycnt = [0] * (10000 + 1)
day, cnt = 1, 0
startRange, endRange = -1, -1
for i in range(1, len(s)):
    if s[i] == "SHOW":
        if startRange <= day <= endRange:
            answer += "\n" + str(0)
        else:
            answer += "\n" + str(1)
            cnt += 1
            daycnt[day] = daycnt[day - 1] + cnt
            preDay = day - m
            if preDay < 0:  # 인덱스를 벗어나면 0 인덱스를 가리키도록 합니다.
                preDay = 0
            if daycnt[day] - daycnt[preDay] >= n:
                cnt = 0
                startRange = day
                endRange = day + m
    elif s[i] == "NEGATIVE":
        answer += "\n" + str(0)
        cnt = 0
        startRange = day
        endRange = day + m
    elif s[i] == "NEXT":
        day += 1
        cnt = 0
        daycnt[day] = daycnt[day - 1] + cnt
        answer += "\n" + "-"
    elif s[i] == "EXIT":
        answer += "\n" + "BYE"
        break
    else:
        answer += "\n" + "ERROR"

print(answer)
