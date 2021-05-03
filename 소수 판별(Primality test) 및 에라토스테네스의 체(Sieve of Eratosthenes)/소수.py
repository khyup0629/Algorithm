# 에라토스테네스의 체 알고리즘을 이용해 구간 내의 소수를 찾는다.
# 계산 시간을 단축하기 위해 소수 배열의 0번째 원소를 최솟값으로 출력한다.
# (소수 배열에 작은 소수부터 순서대로 들어가므로)

import math
m = int(input())
n = int(input())

prime_num = [True] * (n + 1)
prime_num[1] = False  # 1은 소수가 아니다.
for i in range(2, int(math.sqrt(n))+1):
    if prime_num[i]:
        j = 2
        while i * j <= n:
            if prime_num[i*j]:
                prime_num[i*j] = False
            j += 1

# 소수를 작은 수부터 순서대로 넣기
prime = []
for i in range(m, n+1):
    if prime_num[i]:
        prime.append(i)

if not prime:  # 구간 내에 소수가 없다면,
    print(-1)
else:
    print(sum(prime))
    print(prime[0])

"""
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 
이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1 
60
100
예제 출력 1 
620
61
예제 입력 2 
64
65
예제 출력 2 
-1
"""