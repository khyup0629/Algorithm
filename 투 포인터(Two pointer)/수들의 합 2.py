n, m = map(int, input().split())

array = list(map(int, input().split()))

end, interval_sum, cnt = 0, 0, 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += array[end]
        end += 1
    if interval_sum == m:
        cnt += 1
    interval_sum -= array[start]

print(cnt)
