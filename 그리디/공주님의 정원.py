def date_to_days(month, day):
    days = 0
    if month == 1:
        days += day
    else:
        for j in range(1, month):
            if j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12:
                days += 31
            elif j == 4 or j == 6 or j == 9 or j == 11:
                days += 30
            else:
                days += 28
        days += day
    return days

n = int(input())

d = []
for i in range(n):
    x = input().split(' ')
    a = [date_to_days(int(x[0]), int(x[1])), date_to_days(int(x[2]), int(x[3]))]
    d.append(a)
d.sort()
# print(d)
# d : 각 꽃들의 시작과 끝을 일 단위로 나타낸 것

end = 60
startday = date_to_days(3, 1)
endday = date_to_days(11, 30)

# print(startday,endday)

flowerperiod = []
for i in range(startday, endday+1):
    flowerperiod.append(i)

flower = 0
temp = 0
w = -1
# w < n 은 모든 꽃을 다 체크해봤을 때 기간이 남았을 경우 반복문을 멈춰야 하는 조건
while end <= endday and w < n:
    changed = 0
    w += 1
    for i in range(w, n):
        if d[i][0] > end:
            break
        if temp < d[i][1]:
            temp = d[i][1]
            w = i
            changed = 1
    if changed == 1:
        end = temp
        flower += 1
    else:
        flower = 0
        break

print(flower)
# print(resultperiod)
# print(flowerperiod)
'''
(실패)

def date_to_days(month, day):
    days = 0
    if month == 1:
        days += day
    else:
        for j in range(1, month):
            if j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12:
                days += 31
            elif j == 4 or j == 6 or j == 9 or j == 11:
                days += 30
            else:
                days += 28
        days += day
    return days

n = int(input())

d = []
for i in range(n):
    x = input().split(' ')
    a = [date_to_days(int(x[0]), int(x[1])), date_to_days(int(x[2]), int(x[3]))]
    d.append(a)
d.sort()
# print(d)
# d : 각 꽃들의 시작과 끝을 일 단위로 나타낸 것

startday = date_to_days(3, 1)
endday = date_to_days(11, 30)

# print(startday,endday)

flowerperiod = []
for i in range(startday, endday+1):
    flowerperiod.append(i)

flower = 0
while flowerperiod != []:
    best = 0
    resultperiod = []
    for i in range(n):
        w = 0
        dperiod = []
        for j in range(d[i][0], d[i][1]):
            if flowerperiod.count(j) == 1:
                w += 1
                dperiod.append(j)
        # print(dperiod)
        if w > best:
            best = w
            resultperiod = dperiod
    lengthresultperiod = len(resultperiod)
    for i in range(lengthresultperiod):
        if flowerperiod.count(resultperiod[i]) == 1:
            flowerperiod.remove(resultperiod[i])
    # print(flowerperiod)
    flower += 1
    if flower == (n+1):
        flower = 0
        break

print(flower)
# print(resultperiod)
# print(flowerperiod)
'''