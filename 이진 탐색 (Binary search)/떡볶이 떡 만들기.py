# 입력값의 범위가 0~10억이므로 탐색 범위가 넓다.
# 이러한 넓은 탐색 범위는 이진 탐색으로 알고리즘을 짠다.

# 떡의 개수, 요청한 떡의 길이
n, m = map(int, input().split())
# 떡의 높이 정보
array = list(map(int, input().split()))

# 이진 탐색의 시작점과 끝점
start = 0
end = max(array)

result = 0
# 이진 탐색에서는 시작점이 끝점보다 커지게 되면 계산 종료.
while start <= end:
    total = 0
    mid = (start+end) // 2
    for i in array:
        if i > mid:  # 떡이 중간값보다 길면 자르고 합친다.
            total += (i - mid)
    if total >= m:  # 요청한 떡의 길이보다 길거나 같을 경우
        result = mid  # 결과값 갱신
        start = mid + 1  # 시작점 위로 갱신
    else:
        end = mid - 1  # 끝점 아래로 갱신

print(result)

"""
예제 입력
4 6
19 15 6 17
예제 출력
15
"""