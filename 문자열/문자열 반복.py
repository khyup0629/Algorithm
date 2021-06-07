t = int(input())

for _ in range(t):
    r, s = input().split()
    ans = ''
    for i in s:
        for j in range(int(r)):
            ans += i

    print(ans)

# 문제 : https://www.acmicpc.net/problem/2675
