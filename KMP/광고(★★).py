l = int(input())
s = input()

# 실패 함수
j = 0
pi = [0] * l
for i in range(1, l):
    # aabaaa 의 경우 pi가 010122가 나오는데
    # 이렇게 반복문을 넣어주는 이유는 예를 들어
    # aab와 aaa 비교의 경우 끝에 b/a가 다르므로
    # 이전에 구했던 부분 문자열 길이를 통해
    # j의 위치를 재설정함으로써 부분 문자열 길이를 구할 수 있다.
    while j > 0 and s[j] != s[i]:
        j = pi[j-1]
    if s[j] == s[i]:
        j += 1
        pi[i] = j

print(l-pi[l-1])  # 전체 길이 - 일치하는 문자열의 가장 긴 길이

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