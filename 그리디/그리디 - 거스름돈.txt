a = int(input())

n = 1000 - a

d = []
for i in range(6):
    d.append(0)

d[0] = n // 500
n = n % 500
d[1] = n // 100
n = n % 100
d[2] = n // 50
n = n % 50
d[3] = n // 10
n = n % 10
d[4] = n // 5
n = n % 5
d[5] = n // 1
n = n % 1

sum = 0
for i in d:
    sum = sum + i

print(sum)