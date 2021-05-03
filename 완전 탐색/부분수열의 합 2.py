# 부분 수열 : 주어진 수열 중 일부 원소들을 뽑아내어 모은 수열.
# 연속 수열이 아님!
# 1. 왼쪽과 오른쪽으로 수열을 나눈다.
# 2. 왼쪽의 부분 수열의 합을 계산하면서 s와 같은 것을 카운트
# 2-1. 딕셔너리에 {왼쪽의 부분 수열의 합 : 개수} 형태로 저장
# 3. 오른쪽의 부분 수열의 합을 하나씩 탐색하고 s와 같은 것을 카운트하면서,
# 4. (목표값(s) - 오른쪽 현재 탐색 중인 부분 수열의 합(sum(j)))이
# '왼쪽의 부분 수열의 합' 딕셔너리에 존재한다면, value값인 개수만큼 카운트.
from itertools import combinations
n, s = map(int, input().split())

array = list(map(int, input().split()))
cnt = 0
# 왼쪽과 오른쪽으로 수열을 나눈다.
left = array[0:n//2]
right = array[n//2:n]

# 왼쪽 수열의 부분수열의 합과 개수를 딕셔너리에 넣는다.
left_sum = {}
for i in range(1, len(left)+1):
    combi = list(combinations(left, i))
    # {부분수열의 합 : 개수} 형태
    for j in combi:
        left_sum[sum(j)] = left_sum.get(sum(j), 0) + 1
        # 왼쪽 수열의 부분 수열 중에서 합이 s와 같은 것을 카운트.
        if sum(j) == s:
            cnt += 1

# 오른쪽 수열의 부분 수열의 합을 하나씩 계산한다.
for i in range(1, len(right)+1):
    combi = list(combinations(right, i))
    for j in combi:
        # 오른쪽 수열의 부분 수열 중에서 합이 s와 같은 것을 카운트.
        if sum(j) == s:
            cnt += 1
        # 왼쪽 수열의 딕셔너리 중에서 (s - 오른쪽 수열의 현재 부분 수열의 합)의 값이 존재한다면,
        # 왼쪽 수열의 부분 수열의 합 중 (s - 오른쪽 수열의 현재 부분 수열의 합)의 개수만큼 카운트.
        if left_sum.get(s-sum(j)):
            cnt += left_sum.get(s-sum(j))


print(cnt)

"""
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 
그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 40, |S| ≤ 1,000,000) 
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 입력 1 
5 0
-7 -3 -2 5 8
예제 출력 1 
1
"""