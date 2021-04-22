# 탐색 범위가 10억 단위이므로 넓다 -> 이진 탐색 고려
# 이진 탐색 관련 표준 라이브러리를 사용하면
# 시간 복잡도 O(logN)을 보장할 수 있다.
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

# 원소의 개수, 특정 수
n, x = map(int, input().split())

# 리스트 입력
array = list(map(int, input().split()))
# x가 리스트 안에서 가장 먼저 들어갈 수 있는 부분과
# 가장 뒤에 들어갈 수 있는 부분의 인덱스를 찾는다.
start = bisect_left(array, x)
end = bisect_right(array, x)
# 두 값의 차이가 특정 수(x)의 개수
result = end - start
if result == 0:  # 원소가 없으면 start = end 이므로 result = 0
    print(-1)  # -1 출력
else:
    print(result)

"""
예제 입력 1
7 2
1 1 2 2 2 2 3
예제 출력 1
4
예제 입력 2
7 2
1 1 3 3 3 3 3
예제 출력 2
-1
"""
