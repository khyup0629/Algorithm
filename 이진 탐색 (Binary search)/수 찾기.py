# count 함수를 사용하게 되면 시간 복잡도가 O(NM)으로
# 최대 입력값으로 받게 될 경우 100억 번의 계산 횟수가 책정된다.
# 따라서 이진 탐색의 표준 라이브러리인 bisect 를 사용해서
# 개수를 탐색하게 되면 계산 과정을 확연히 줄일 수 있다.

from bisect import bisect_left, bisect_right
n = int(input())
arrFirst = list(map(int, input().split()))
m = int(input())
arrSecond = list(map(int, input().split()))

arrFirst.sort()

for i in range(m):
    idxLeft = bisect_left(arrFirst, arrSecond[i])
    idxRight = bisect_right(arrFirst, arrSecond[i])
    if idxRight - idxLeft > 0:
        print(1)
    else:
        print(0)

# 문제 : https://www.acmicpc.net/problem/1920        

"""
# (count 함수를 사용해 찾게 되면 시간 초과)
import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

m = int(input())

count = list(map(int, input().split()))

for i in count:
    if array.count(i) > 0:
        print(1)
    else:
        print(0)

"""
