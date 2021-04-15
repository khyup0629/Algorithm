# 문제 해결 아이디어 : '퇴사 해결 아이디어' 사진 참조

n = int(input())

data = [list(map(int, input().split(' '))) for _ in range(n)]

# 현재 일까지 받을 수 있는 모든 수익의 경우가 저장됨
cost = [[0] for _ in range(n)]
# 초기값, 어떠한 수익도 받을 수 없다면 0을 표시하기 위함
result = [0]
# 1 ~ n 일까지 차례대로 고려
for i in range(n):
    # i일 까지 얻을 수 있는 최대 수익 = i일 전까지 얻을 수 있는 수익 중 가장 큰 값 + i일에 받을 수 있는 수익
    new_cost = max(cost[i])+data[i][1]
    # (i일 + i일의 상담 기간)이 n일을 초과하게 되면 반복문 스킵
    if i+data[i][0] > n:
        continue
    # 초과하지 않는다면 result 에 현재 수익을 저장
    result.append(new_cost)
    # (i일 + i일의 상담 기간)일부터 현재 new_cost 수익을 받을 수 있으므로
    # 그 이후 일에 대해 new_cost(i일 까지 얻을 수 있는 최대 수익) 저장
    for j in range(i+data[i][0], n):
        cost[j].append(new_cost)

print(max(result))
