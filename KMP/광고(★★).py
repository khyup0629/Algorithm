# 아래의 입력 예제를 토대로 차근차근 따라가보면 실패함수에 대해서 이해할 수 있습니다.

l = int(input())
s = input()

# 실패 함수
j = 0
pi = [0] * l
for i in range(1, l):
    while j > 0 and s[i] != s[j]:
        j = pi[j-1]
    if s[i] == s[j]:
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
