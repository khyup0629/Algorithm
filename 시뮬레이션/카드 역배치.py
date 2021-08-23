# 쉬운 시뮬레이션 문제였습니다.
arr = [i for i in range(20+1)]

for _ in range(10):
    a, b = map(int, input().split())
    # 임시 배열에 [a, b] 구간의 arr 값을 추가합니다.
    temp = []
    for i in range(a, b+1):
        temp.append(arr[i])
    # 임시 배열을 뒤집습니다.
    temp = temp[::-1]
    # 다시 arr의 [a, b] 구간을 temp값으로 갱신합니다.
    for i in range(a, b+1):
        arr[i] = temp[i-a]

print(*arr[1:])

# 문제 : https://www.acmicpc.net/problem/10804
