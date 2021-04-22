import sys

input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 소수점은 버리고 가운데
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

"""
예제 입력
10 7
1 3 5 7 9 11 13 15 17 19
예제 출력
4
"""