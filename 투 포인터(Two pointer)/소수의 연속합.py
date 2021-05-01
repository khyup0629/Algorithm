# 1. 자연수 n까지 소수를 찾아서 모은다. 시간 복잡도 : O(NloglogN + N)
# 2. 투 포인터를 이용해 연속합을 구한다. 시간 복잡도 : O(N)
# 3. 연속합이 n과 같다면 카운트 +1
import math

n = int(input())
# 1 ~ n 까지의 소수 판별
prime_num = [True] * (n + 1)  # 초기엔 n 까지의 모든 수가 소수라고 가정.
for i in range(2, int(math.sqrt(n))+1):
    if prime_num[i]:
        # 자신을 제외한 배수를 지운다.
        j = 2
        while i * j <= n:
            prime_num[i*j] = False
            j += 1

# 소수를 array 배열에 따로 담기
array = []
for i in range(2, n+1):
    if prime_num[i]:
        array.append(i)

# 투 포인터
end, interval_sum, cnt = 0, 0, 0
for start in range(len(array)):
    while interval_sum < n and end < len(array):
        interval_sum += array[end]
        end += 1
    if interval_sum == n:
        cnt += 1
    interval_sum -= array[start]

print(cnt)

"""
문제
하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.

3 : 3 (한 가지)
41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
53 : 5+7+11+13+17 = 53 (두 가지)
하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 
7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 
또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)

출력
첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.

예제 입력 1 
20
예제 출력 1 
0
예제 입력 2 
3
예제 출력 2 
1
예제 입력 3 
41
예제 출력 3 
3
예제 입력 4 
53
예제 출력 4 
2
"""