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
