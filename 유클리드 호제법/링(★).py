# 유클리드 호제법을 사용하여 시간 복잡도를 줄여서 최대공약수를 찾는다.
# 기약분수는 분자와 분모의 최대공약수를 나눠서 구할 수 있다.
def gcd(a, b):
    while b != 0:
        n = a % b
        a = b
        b = n
    return a


n = int(input())
lst = list(map(int, input().split()))

for i in range(1, n):
    g = gcd(lst[0], lst[i])
    print("{0}/{1}".format(lst[0]//g, lst[i]//g))

# 문제 : https://www.acmicpc.net/problem/3036
