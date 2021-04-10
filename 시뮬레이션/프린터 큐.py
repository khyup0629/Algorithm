Testcase = int(input())

result_group = []
for i in range(Testcase):
    N, M = map(int, input().split(' '))
    value = input().split(' ')

    # que = [0, 1, 2, 3, 4, ...]
    # value 가 조정될 때 같은 위치가 조정된다
    que = []
    for j in range(N):
        que.append(j)

    result = 0
    while True:
        changed = 0
        for j in range(1, len(que)):
            temp_value = value[0]
            temp_que = que[0]
            if value[0] < value[j]:
                value.remove(value[0])
                value.append(temp_value)
                que.remove(que[0])
                que.append(temp_que)
                changed = 1
                break
        if changed == 0:
            value.remove(value[0])
            que.remove(que[0])
            result += 1
        if que.count(M) == 0:
            break

    result_group.append(result)

for i in result_group:
    print(i)
