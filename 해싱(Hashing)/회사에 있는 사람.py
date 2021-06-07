# 사전 순 정렬 : 대문자 A~Z -> 소문자 a~z
# 딕셔너리에서 del 함수는 시간복잡도 O(1)
import sys
input = sys.stdin.readline

n = int(input())

member = {}
for _ in range(n):
    name, stand = input().split()
    if stand == 'enter':
        member[name] = name
    else:
        del member[name]

s = sorted(member.keys(), reverse=True)

for i in s:
    print(i)

# 문제 : https://www.acmicpc.net/problem/7785
