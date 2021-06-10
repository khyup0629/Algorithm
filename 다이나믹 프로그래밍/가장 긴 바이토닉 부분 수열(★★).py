# 문제 풀이 아이디어
# 원래의 수열로 각 수까지 가장 긴 증가하는 부분 수열을 구한다.
# 뒤집은 수열로 각 수까지 가장 긴 감소하는 부분 수열을 구한다.
# (수열을 뒤집어서 가장 긴 증가하는 부분 수열을 구한 뒤 다시 뒤집으면 가장 긴 감소하는 부분 수열이 된다.)
# 각 수까지 가장 긴 증가하는 부분 수열 + 가장 긴 감소하는 부분 수열 - 1의 값 중 최댓값이 정답.
n = int(input())

num = list(map(int, input().split()))  # 원래 수열
rev_num = num[::-1]  # 뒤집은 수열

increase = [1] * n
decrease = [1] * n
for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if rev_num[i] > rev_num[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

_max = 0
for i in range(n):
    _max = max(_max, increase[i] + decrease[n-i-1] - 1)

print(_max)

# 문제 : https://www.acmicpc.net/problem/11054

"""
원래수열    1  5  2  1  4  3  4  5  2  1
increase  [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
뒤집은수열   1  2  5  4  3  4  1  2  5  1
decrease  [1, 2, 3, 3, 3, 4, 1, 2, 5, 1]
decrease를 뒤집으면
decrease  [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]
increase[i] + decrease[i] - 1의 최댓값을 구한다.
"""