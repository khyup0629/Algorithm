# 부분 수열 : 주어진 수열 중 일부 원소들을 뽑아내어 모은 수열.
# 연속 수열이 아님!
from itertools import combinations
n, s = map(int, input().split())

array = list(map(int, input().split()))

combi = []
_sum = {}
for i in range(1, n+1):
    # 조합 1개 짜리인 (-7,)도 sum을 해주게 되면 정상적으로 -7의 결과값이 나온다.
    combi = list(combinations(array, i))
    for j in combi:
        _sum[sum(j)] = _sum.get(sum(j), 0) + 1

print(_sum.get(s, 0))

"""
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 
S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 입력 1 
5 0
-7 -3 -2 5 8
예제 출력 1 
1
"""