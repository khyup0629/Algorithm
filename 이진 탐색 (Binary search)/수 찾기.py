# count 함수를 사용하게 되면 시간 복잡도가 O(NM)으로
# 최대 입력값으로 받게 될 경우 100억 번의 계산 횟수가 책정된다.
# 따라서 이진 탐색의 표준 라이브러리인 bisect 를 사용해서
# 개수를 탐색하게 되면 계산 과정을 확연히 줄일 수 있다.

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline  # 입력을 빠르게 받아서 시간 단축

n = int(input())

array = list(map(int, input().split()))

m = int(input())

count = list(map(int, input().split()))
array.sort()  # 정렬된 리스트에 대해서 bisect 를 써야하므로

for i in count:
    start = bisect_left(array, i)
    end = bisect_right(array, i)
    if (end - start) > 0:
        print(1)
    else:
        print(0)

"""
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1
"""

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