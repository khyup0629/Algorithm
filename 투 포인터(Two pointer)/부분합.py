# 투 포인터를 사용한 알고리즘
# 수의 개수, 기준값의 범위
n, s = map(int, input().split())
array = list(map(int, input().split()))

end = 0
_min = int(1e9)  # 무한대의 값
interval_sum = 0  # 부분 합

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += array[end]
        end += 1  # 현재까지의 부분합보다 +1만큼 나아간다.
    # 뒷부분을 위한 조건. end가 배열 끝에 닿고 start만 올라오는 경우
    # 뒷부분에서도 조건을 만족한다면 최솟값을 갱신해야하기 때문.
    if interval_sum >= s:
        _min = min(_min, end - start)
    interval_sum -= array[start]

# _min이 무한대의 값을 가진다면 반복 내에 조건을 만족하는 경우가 없었다는 뜻이므로 합을 만드는 것이 불가능.
if _min == int(1e9):
    print(0)
else:
    print(_min)

"""
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 
가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 
수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

예제 입력 1 
10 15
5 1 3 5 10 7 4 9 2 8
예제 출력 1 
2
예제 입력 2
10 100000
5 1 3 5 10 7 4 9 2 8
예제 출력 2
0
"""