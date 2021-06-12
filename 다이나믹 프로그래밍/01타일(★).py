# 각 과정마다 15746의 나머지를 구해주지 않으면 메모리 초과가 발생한다.
n = int(input())

d = [0] * (n + 1)
d[1] = 1
if n >= 2:
    d[2] = 2
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2]) % 15746

print(d[n] % 15746)

# 문제 : https://www.acmicpc.net/problem/1904
