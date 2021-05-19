# 최대한 전에 풀었던 코드를 참고하지 않고 풀어보려 하였으나
# 시간 초과가 발생하였고, KMP가 아닌가 싶어 라빈-카프 알고리즘으로 시도하였으나
# KMP보다 더 빨리 시간 초과가 발생해 다시 KMP로 돌아와서 고민하다가
# 전의 코드를 약간 참고해서 풀 수 있었다.
# i는 S와 P의 비교 시작점, j를 +시키면서 비교해준다.
# 이렇게 해야 중복되는 문자열은 생략하고 비교가 가능하다.

# S < P의 경우는 고려하지 않아도 된다.
# (문제에 설명은 없으나 고려하지 않아도 답이 맞았다.)
S = input()
P = input()

# 실패 함수
pi = [0] * len(P)
j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = pi[j-1]
    if P[i] == P[j]:
        j += 1
        pi[i] = j

# KMP
i = 0
j = 0
cnt = 0
while i+j < len(S):
    if S[i+j] == P[j]:
        j += 1
    else:
        if j == 0:
            i += 1
        else:
            i += j - pi[j-1]
            j = pi[j-1]
    if j == len(P):
        cnt += 1
        break

print(cnt)

# 문제 : https://www.acmicpc.net/problem/16916

"""
# 라빈-카프 : 시간초과
S = input()
P = input()

cnt = 0
value_S, value_P = 0, 0
n = len(P)
arr = [i for i in range(n-1, -1, -1)]
for i in range(n):
    value_P += (ord(P[i]) * (2 ** arr[i]))
    value_S += (ord(S[i]) * (2 ** arr[i]))

if value_S == value_P:
    cnt += 1

start = 1
end = len(P)
while end < len(S):
    value_S = 2 * (value_S - ord(S[start-1]) * (2 ** arr[0])) + ord(S[end])
    if value_S == value_P:
        cnt += 1
        break
    start += 1
    end += 1

print(cnt)

"""
