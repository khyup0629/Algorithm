# '가장 긴 증가하는 부분 수열 3'의 확장 문제.
# 수열에 속해있는 어떤 수의 인덱스와 대응하도록 dp 테이블을 만든다.
# dp 테이블에는 어떤 수가 가질 수 있는 최대 길이가 저장된다.
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n  # 어떤 수가 가질 수 있는 최대 길이가 저장된다.

# temp에 속해있는 원소들로는 가장 긴 증가하는 부분 수열이라 할 수 없는 임시 수열.
temp = [arr[0]]
for i in range(1, n):
    if temp[-1] < arr[i]:
        temp.append(arr[i])
        dp[i] = len(temp)
    else:
        idx = bisect_left(temp, arr[i])
        temp[idx] = arr[i]
        dp[i] = idx + 1

maxLen = max(dp)  # 가장 증가하는 부분 수열의 길이
print(maxLen)

resultArr = []  # 수가 내림차순으로 저장된다.
for i in range(n-1, -1, -1):  # DP 테이블의 뒤에서부터 확인하면서
    if dp[i] == maxLen:  # 최대 길이와 dp 테이블의 해당하는 인덱스가 같다면,
        resultArr.append(arr[i])  # array 중 해당하는 인덱스의 수를 저장한다.
        maxLen -= 1

# 내림차순을 뒤집어 오름차순으로 만든 다음 출력한다.
resultArr = resultArr[::-1]
for num in resultArr:
    print(num, end=' ')

# 문제 : https://www.acmicpc.net/problem/14003

"""
풀이 예시)

index   0   1   2   3   4   5   6
------------------------------------
DP      1   2   1   2   3   1   2   
array   30  35  10  15  20  -10 0

1. temp = [30], dp[0] = 1
2. 35가 30보다 크므로 temp의 끝에 더한다.
temp = [30, 35], dp[1] = 2
3. 10은 35보다 작으므로 이진탐색을 통해 temp에 들어갈 수 있는 자리를 찾고(0), +1을 해서 dp[2]에 저장한다. 
temp = [10, 35], dp[2] = 1
4. 15는 35보다 작으므로 이진탐색을 통해 temp에 들어갈 수 있는 자리를 찾는다.(1), +1을 해서 dp[3]에 저장한다. 
temp = [10, 15], dp[3] = 2
5. 20은 15보다 크므로 temp의 끝에 더한다. 
temp = [10, 15, 20], dp[3] = 3
6. 과정을 반복하고 가장 긴 증가하는 부분 수열의 원소를 찾기 위해
dp의 뒤에서부터 최대 길이와 같은 것을 찾고, 찾으면 최대 길이 변수를 -1하면서 내림차순으로 찾는다.
result = [20, 15, 10]
7. 출력할 땐 result의 뒤에서부터 출력한다.
"""
