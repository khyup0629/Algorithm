# 입력값의 범위를 보면 10억 이상씩 큰 것으로 볼 수 있으므로
# 이진 탐색을 수행해서 알고리즘 코딩
# PyPy3 제출

n, m = map(int, input().split())
woodLen = list(map(int, input().split()))

start, end = 0, max(woodLen)
ans = 0  # 정답
while start <= end:
    mid = (start + end) // 2

    takeWood = 0  # 가져갈 나무의 총 길이
    for wood in woodLen:
        if wood > mid:  # 기준을 넘어가는 것만 자릅니다.
            takeWood += (wood - mid)

    if takeWood >= m:
        ans = mid  # 적어도 m개를 가져가야 하므로 m개 이상을 가져가면 답을 갱신합니다.
        start = mid + 1
    else:
        end = mid - 1

print(ans)

# 문제 : https://www.acmicpc.net/problem/2805
