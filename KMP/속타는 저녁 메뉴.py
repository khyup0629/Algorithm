# KMP + 기약분수(최대공약수)를 통해 풀어야 하는 알고리즘
# 기약분수를 구하는 아이디어는
# 분자의 수부터 1까지 -1씩 아래로 내려가면서 분자와 분모가 모두 나누어 떨어지는 최초의 수로
# 나눈 몫을 각각 분자와 분모로 하면 된다.

n = int(input())
p = list(input().split())  # 부분 문자열
s = list(input().split())

s.extend(s)  # 전체 문자열

pi = [0] * n
b = 0
for a in range(1, len(p)):
    while b > 0 and p[a] != p[b]:
        b = pi[b-1]
    if p[a] == p[b]:
        b += 1
        pi[a] = b

i, j = 0, 0
cnt = 0
while i < n:
    if s[i+j] != p[j]:
        if j == 0:
            i += 1
        else:
            i += j - pi[j-1]
            j = pi[j-1]
    else:
        j += 1
    if j == len(p):  # 부분 문자열의 길이와 같다면,
        cnt += 1
        i += j - pi[j-1]
        j = pi[j-1]

# 기약분수 형태로 나타내기
x, y = 1, 1
for i in range(cnt, 0, -1):
    if cnt % i == 0 and n % i == 0:
        x = cnt // i
        y = n // i
        break

print("{0}/{1}".format(x, y))

# 문제 : https://www.acmicpc.net/problem/11585
