l = int(input())
s = input()

# 실패 함수
j = 0
pi = [0] * l
for i in range(1, l):
    while j > 0 and s[j] != s[i]:
        j = pi[j-1]
    if s[j] == s[i]:
        j += 1
        pi[i] = j

print(l-pi[l-1])  # 전체 길이 - 일치하는 문자열의 가장 긴 길이

# 문제 : https://www.acmicpc.net/problem/1305

"""
11
abaaabaaaba
11
abaaaabaaaa
11
abacabacaba
11
aabaacaabaa
"""
