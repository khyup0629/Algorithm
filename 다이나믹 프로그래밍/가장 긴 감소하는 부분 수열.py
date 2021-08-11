# 원래의 수열을 뒤집은 수열을 만들어서 뒤집은 수열의 가장 긴 증가하는 수열을 만든다.
# DP 방법과 이진 탐색의 방법으로 문제를 풀 수 있다.
n = int(input())

A = list(map(int, input().split()))
rev_A = A[::-1]

dp = [1] * n
for i in range(n):
    for j in range(i):
        if rev_A[i] > rev_A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 문제 : https://www.acmicpc.net/problem/11722

# 원래의 수열에서 -를 붙여 음수로 만든 뒤 증가하는 수열로 만들어서 풀 수도 있습니다.
n = int(input())

arr = list(map(int, input().split()))
arr = [-arr[i] for i in range(n)]
dp = [1] * n

for i in range(n):
    for j in range(i+1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
