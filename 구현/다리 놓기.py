t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    x, y = 1, 1
    for i in range(b, b-a, -1):
        x *= i
    for i in range(a, 0, -1):
        y *= i
    print(x // y)

# 문제 : https://www.acmicpc.net/problem/1010
