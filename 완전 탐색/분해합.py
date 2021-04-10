# N의 범위가 1 <= N <= 1,000,000
# 서버 계산 횟수는 1초에 20,000,000
# 최대로 어림잡아 계산해도 7,000,000 이므로
# 기준치인 2초(40,000,000)안에 충분히 계산 가능

N = int(input())

result = 0
for i in range(1, N):
    element = list(str(i))
    hap = i
    for j in element:
        hap += int(j)
    if hap == N:
        result = i
        break

print(result)
