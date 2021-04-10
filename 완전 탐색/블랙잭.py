N, M = map(int, input().split(' '))

num = input().split(' ')

num.sort()

temp = 300000

for i in range(N - 2):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            hap = int(num[i]) + int(num[j]) + int(num[k])
            # 합이 M을 넘지 않으면서 최대가 되는 합
            if hap > M:
                continue
            dif = M - hap
            if temp > dif:
                temp = dif
                result = hap

print(result)
