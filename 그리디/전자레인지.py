import sys

T = int(sys.stdin.readline())

A = 5 * 60
B = 1 * 60
C = 10

count_A = 0
count_B = 0
count_C = 0

# T가 10으로 딱 맞아떨어지지 않으면 T를 맞출 수 없으므로 조건문 활용
if T % 10 == 0:
    while T != 0:
        if T >= A:
            T -= A
            count_A += 1
        elif T >= B:
            T -= B
            count_B += 1
        else:
            T -= C
            count_C += 1
    print(count_A, count_B, count_C)
else:
    print(-1)