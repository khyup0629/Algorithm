import sys
# 힙 정렬과 우선순위 큐를 위한 라이브러리 heapq
# 파이썬에서는 min_heapify() 로 동작
import heapq
input = sys.stdin.readline


def heapsort(iterable):
    h = []
    result = []
    # 힙 정렬 수행
    # heapq.heappush(리스트, 값) : '리스트' 에 '값'을 힙 정렬로 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    # heapq.heappop(리스트) : '리스트' 의 맨 앞의 원소를 뽑아냄.
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


# 입력값의 개수
n = int(input())
array = []
# 입력 받은 숫자를 array 에 차례대로 기록
for _ in range(n):
    array.append(int(input()))
# 힙 정렬 수행한 후 정렬된 리스트를 res 에 저장
res = heapsort(array)

for i in res:
    print(i)

"""
# 최대 힙 구현 방법
import sys
import heapq
input = sys.stdin.readline


def heapsort(iterable):
    h = []
    result = []
    # 힙 정렬 수행
    # heapq.heappush(리스트, 값) : '리스트' 에 '값'을 힙 정렬로 삽입
    for value in iterable:
        heapq.heappush(h, -value)  # 양수에 -를 붙이게 되면 큰 수가 오히려 더 작아지게 된다
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    # heapq.heappop(리스트) : '리스트' 의 맨 앞의 원소를 뽑아냄.
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))  # 다시 -를 붙인 값을 뽑아내면서 원래 수로 만들어준다.
    return result


# 입력값의 개수
n = int(input())
array = []
# 입력 받은 숫자를 array 에 차례대로 기록
for _ in range(n):
    array.append(int(input()))
# 힙 정렬 수행한 후 정렬된 리스트를 res 에 저장
res = heapsort(array)

for i in res:
    print(i)

"""