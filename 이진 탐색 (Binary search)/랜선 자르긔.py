# 랜선의 길이의 범위는 자연수이므로 최솟값은 1입니다.
# 따라서 초기 start 값은 1입니다.

k, n = map(int, input().split())

cableLen = []
for i in range(k):
    num = int(input())
    cableLen.append(num)

start, end = 1, max(cableLen)  # 랜선의 길이의 범위는 자연수이므로 최솟값은 1입니다.
ans = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for cable in cableLen:
        cnt += (cable // mid)

    if cnt >= n:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)

# 문제 : https://www.acmicpc.net/problem/1654

"""
고려할 반례

입력 예시
1 1
1

출력 예시
1
"""
