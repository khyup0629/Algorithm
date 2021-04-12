def gcd(x, y):
    # x < y
    if y % x == 0:
        return x
    temp = y % x
    return gcd(temp, x)


t = int(input())

result_group = []
for k in range(t):
    data = map(int, input().split(' '))
    number = list(data)
    n = number[0]
    number.remove(n)
    number.sort()
    result = 0

    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            # number[i] < number[j]
            result += gcd(number[i], number[j])
    result_group.append(result)

for k in result_group:
    print(k)
