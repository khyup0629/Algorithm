출처 : [한빛미디어] 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈 저)

---
# 이진 탐색 (Binary Search)

+ 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
+ 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
+ (순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인)

+ 완전 탐색 문제 같은데 입력값의 범위나 계산 횟수가 상당히 크면 **이진 탐색을 고려**해야 한다.

## 1. 이진 탐색의 시간 복잡도

+ 단계마다 탐색 범위를 2로 나누는 것과 동일
  + 예를 들어 초기 데이터 개수가 32개이면, 다음 탐색에는 16개, 8개, 4개로 절반씩 줄어든다.
+ 시간 복잡도는 **O(logN)**

### 이진 탐색 반복문 구현 방법
``` python
# array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# target = 7

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # 소수점은 버리고 가운데
        if array[mid] == target:  # 원하는 수이면 mid값을 반환
            return mid
        elif array[mid] > target:  # 원하는 수보다 크면
            end = mid - 1  # 탐색 범위를 밑으로 좁힌다.
        else:  # 원하는 수보다 작으면
            start = mid + 1  # 탐색 범위를 위로 좁힌다.
    return None

# mid = 4
```

## 2. Bisect 라이브러리
``` python
from bisect import bisect_left, bisect_right

bisect_left(a, x)  # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
bisect_right(a, x)  # 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환
```
+ 위의 라이브러리를 활용해서 배열에서 **특정 범위에 속하는 데이터 개수를 구할 수 있다.**

## 3. 파라메트릭 서치

+ 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
  + 예시 : 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
+ 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 **이진 탐색을 이용하여 해결 가능**

### 특정 수의 개수(파라메트릭 서치)

+ 오름차순 정렬된 배열 내에서 특정 수의 개수를 찾는 문제이다.
``` python
# 탐색 범위가 10억 단위이므로 넓다 -> 이진 탐색 고려
# 이진 탐색 관련 표준 라이브러리를 사용하면 시간 복잡도 O(logN)을 보장할 수 있다.
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
```
[위로](#이진-탐색-Binery-Search)

---
