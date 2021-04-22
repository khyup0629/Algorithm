# 입력값의 범위를 보면 10억 이상씩 큰 것으로 볼 수 있으므로
# 이진 탐색을 수행해서 알고리즘 코딩
# PyPy3 제출

import sys
input = sys.stdin.readline

# 나무의 수, 집으로 가져가려고 하는 나무의 길이
n, m = map(int, input().split())
# 나무의 높이
array = list(map(int, input().split()))
# 나무의 시작점과 끝점
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2  # 소숫점 이하 자리 버림
    for i in array:
        if i > mid:  # 기준을 넘어가는 것만 자른다
            total += (i - mid)
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
