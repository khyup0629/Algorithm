while True:
    s = input()
    if s == '.':
        break
    n = len(s)
    pi = [0] * n
    b = 0
    for a in range(1, n):
        while b > 0 and s[a] != s[b]:
            b = pi[b-1]
        if s[a] == s[b]:
            b += 1
            pi[a] = b

    l = n - pi[-1]

    if n % l == 0:
        print(n // l)
    else:
        print(1)

# 문제 : https://www.acmicpc.net/problem/4354
