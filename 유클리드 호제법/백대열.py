def gcd(a, b):  # 유클리드 호제법
    while b != 0:
        n = a % b
        a = b
        b = n
    return a


n, m = map(int, input().split(':'))

g = gcd(n, m)
print('{0}:{1}'.format(n//g, m//g))

# 문제 : https://www.acmicpc.net/problem/14490
