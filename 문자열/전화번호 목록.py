t = int(input())

for _ in range(t):
    n = int(input())
    num = []
    for _ in range(n):
        a = input()
        num.append(a)

    num.sort()

    ans = 'YES'
    for i in range(n-1):
        string = num[i+1].replace(num[i], '*')
        if string[0] == '*':
            ans = 'NO'
            break

    print(ans)

# 문제 : https://www.acmicpc.net/problem/5052
