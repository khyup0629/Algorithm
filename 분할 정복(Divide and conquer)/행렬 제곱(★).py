# B = 1일 경우에 1000의 나머지를 구하지 않는 반례가 있었다. 여기서 해맸다.
# 문제 풀이 아이디어(이진트리를 그려서 이해하면 쉽다)
# 1. 행렬을 제곱하는 것이므로 제곱만큼 행렬을 나열하고 앞에서부터 2개씩 짝지으면 하나가 남거나 남지 않게 된다.
# 2. 짝지은 2개를 제곱하는 연산을 모두 수행할 필요 없이 모두 같은 값을 나타낼 것이므로 한 번만 수행한다.
# 3. 어느 깊이를 막론하고 만약 하나의 노드가 맨 끝에 남게 되면 그 노드로부터 거슬러 올라오는 모든 노드들의 곱셈이 영향을 받게 된다.
# 4. 따라서, 리프 노드부터 거슬러 올라올 때 4가지의 경우를 고려해야 한다.
#   4-0. 계산은 두 가지를 고려해야 한다.
#       ㅇ 각 깊이의 같은 값을 가지는 노드(result), 각 깊이의 남는 노드 또는 남는 노드가 관여된 노드(rest)
#   4-1. 현재 깊이의 노드 개수가 홀수이고, 이전 깊이까지 홀수였던 적이 있는가.
#       ㅇ 현재 깊이의 가장 마지막 노드의 값 = 이전 깊이의 rest
#       ㅇ 2개씩 짝지어진 노드를 계산
#   4-2. 현재 깊이의 노드 개수가 홀수이고, 이전 깊이까지 홀수였던 적이 없다.
#       ㅇ 현재 깊이의 가장 마지막 노드의 값 = 이전 깊이의 result
#       ㅇ 2개씩 짝지어진 노드를 계산
#   4-3. 현재 깊이의 노드 개수가 짝수이고, 이전 깊이까지 홀수였던 적이 있는가.
#       ㅇ 현재 깊이의 마지막 노드 2개를 곱한다 = 이전 깊이의 result * 이전 깊이의 rest
#       ㅇ 나머지 2개씩 짝지어진 노드를 계산
#       ㅇ 노드 개수가 만약 2개라면 result = rest
#   4-4. 현재 깊이의 노드 개수가 짝수이고, 이전 깊이까지 홀수였던 적이 없다.
#       ㅇ rest 계산 생략.
#       ㅇ 2개씩 짝지어진 노드 계산 = result * result
# 5. result를 출력한다.

n, B = map(int, input().split())
A = []
for _ in range(n):
    arr = list(map(int, input().split()))
    A.append(arr)

rest = [[0] * n for _ in range(n)]  # 맨 끝에 남아있는 노드
t_rest = [[0] * n for _ in range(n)]  # rest가 갱신되기 전 저장될 임시저장소
result = [[0] * n for _ in range(n)]  # 2개씩 짝지어져 곱셈된 노드
for i in range(n):
    for j in range(n):
        result[i][j] = A[i][j]

cnt = B
rest_condition = False  # 초기에는 끝에 노드가 남아있었던 적이 없다.
while cnt != 1:  # 노드 개수가 1개가 되면 종료
    # 4-1. 현재 깊이의 노드 개수가 홀수이고, 이전 깊이까지 홀수였던 적이 있는가.
    if cnt % 2 == 1 and rest_condition:
        rest_condition = True  # 끝에 노드가 남아있었던 적이 있다.
        # rest는 동일하므로 생략
        # 제곱한 값을 result에 넣는다.
        for i in range(n):
            for j in range(n):
                hap = 0
                for k in range(n):
                    # result값이 계산에 영향을 주게 하면 안되기 때문에 임시 저장소인 A값을 둔다.
                    hap += A[i][k] * A[k][j]
                result[i][j] = hap % 1000  # 계산과정에서 값이 너무 커지는 것을 방지
        # A값 갱신
        for i in range(n):
            for j in range(n):
                A[i][j] = result[i][j]
        # 남은 노드의 개수를 줄인다.
        cnt = (cnt // 2 + 1)
    # 4-2. 현재 깊이의 노드 개수가 홀수이고, 이전 깊이까지 홀수였던 적이 없다.
    elif cnt % 2 == 1 and not rest_condition:
        rest_condition = True  # 끝에 노드가 남아있었던 적이 있다.
        # rest는 이전 깊이의 result와 같다.
        for i in range(n):
            for j in range(n):
                rest[i][j] = result[i][j]
        # 제곱한 값을 result에 넣는다.
        for i in range(n):
            for j in range(n):
                hap = 0
                for k in range(n):
                    hap += A[i][k] * A[k][j]
                result[i][j] = hap % 1000
        for i in range(n):
            for j in range(n):
                A[i][j] = result[i][j]
        cnt = (cnt // 2 + 1)
    # 4-3. 현재 깊이의 노드 개수가 짝수이고, 이전 깊이까지 홀수였던 적이 있는가.
    elif cnt % 2 == 0 and rest_condition:
        rest_condition = True  # 끝에 노드가 남아있었던 적이 있다.
        # rest는 이전 result * rest
        for i in range(n):
            for j in range(n):
                hap = 0
                for k in range(n):
                    hap += A[i][k] * rest[k][j]
                t_rest[i][j] = hap % 1000
        for i in range(n):
            for j in range(n):
                rest[i][j] = t_rest[i][j]
        # 제곱한 값을 result에 넣는다.
        for i in range(n):
            for j in range(n):
                hap = 0
                for k in range(n):
                    hap += A[i][k] * A[k][j]
                result[i][j] = hap % 1000
        for i in range(n):
            for j in range(n):
                A[i][j] = result[i][j]
        # 노드 개수가 2개만 남았다면
        if cnt == 2:
            # 계산된 rest 값이 곧 result 값
            result = rest
        cnt = (cnt // 2)
    # 4-4. 현재 깊이의 노드 개수가 짝수이고, 이전 깊이까지 홀수였던 적이 없다.
    elif cnt % 2 == 0 and not rest_condition:
        rest_condition = False
        # rest는 아직 존재하지 않으므로 계산하지 않는다.
        # 제곱한 값을 result에 넣는다.
        for i in range(n):
            for j in range(n):
                hap = 0
                for k in range(n):
                    hap += A[i][k] * A[k][j]
                result[i][j] = hap % 1000
        for i in range(n):
            for j in range(n):
                A[i][j] = result[i][j]
        cnt = (cnt // 2)

# B = 1일 경우 while문을 거치지 않으므로 1000의 나머지를 출력하기 위해
# 출력문에도 1000의 나머지를 써준다.
for i in range(n):
    for j in range(n):
        print(result[i][j] % 1000, end=' ')
    print()

# 문제 : https://www.acmicpc.net/problem/10830
