n = int(input())

p = input().split(' ')
for i in range(n):
    p[i] = int(p[i])
# 정렬하기 전에 반드시 int형으로 변환 후 정렬
p.sort()

s = 0
result = 0
for i in range(n):
    s += p[i]
    result += s

print(result)
