n = int(input())

d = []
for i in range(n):
    x, y = map(int, input().split(' '))
    d.append([y, x])

d.sort()

temp = 0
end = d[0][0]
w = 1
for i in range(1, n):
    if d[i][1] >= end:
        w += 1
        end = d[i][0]
print(w)