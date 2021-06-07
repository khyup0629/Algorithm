import sys
input = sys.stdin.readline

n = int(input())

member = []
for i in range(n):
    a, b = input().split()
    member.append((i, int(a), b))

member.sort(key=lambda x: (x[1], x[0]))

for i, age, name in member:
    print(age, name)

# 문제 : https://www.acmicpc.net/problem/10814
