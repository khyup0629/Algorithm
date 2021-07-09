import sys
input = sys.stdin.readline
n = int(input())

file = {}
for _ in range(n):
    text = list(input().strip().split('.'))
    file[text[1]] = file.get(text[1], 0) + 1

s = sorted(file.keys())

for i in s:
    print(i, file[i])

# 문제 : https://www.acmicpc.net/problem/20291
