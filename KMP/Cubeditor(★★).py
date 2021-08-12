# 해싱으로 풀 경우 메모리 초과현상이 나타난다.
# 따라서, KMP 알고리즘을 공부해서 이용했다.
# 부분 문자열 : 부분 수열과는 다르게 투 포인터처럼 연속된 문자열이다.
string = input()

maxLen = 0
for k in range(len(string)):
    s = string[k:]
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    maxLen = max(maxLen, max(pi))

print(maxLen)

# 문제 : https://www.acmicpc.net/problem/1701
