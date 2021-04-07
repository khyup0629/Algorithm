n = int(input())
lst = [0 for i in range(n)]

for i in range(n):
    lst[i] = i + 1

a = input().split(' ')

for i in range(n):
    a[i] = int(a[i])

k2 = 0
k1 = 0
# 오른쪽 밀기
for i in range(3):
    s = a[n-1]
    a.remove(s)
    a.insert(0,s)
    k2 += 1
    if (a[0] - 1) == a[n-1]:
        continue
    else:
        for j in range(1,n):
            if (a[j] - a[j-1]) == 1 or (a[j] - a[j-1]) == -(n - 1):
                continue
            else:
                if ()