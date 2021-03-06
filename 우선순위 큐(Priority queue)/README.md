# 우선순위 큐(Priority Queue)

- 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다.
- 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용한다.

## 우선순위 큐 구현 방법

- 단순히 **리스트를 이용**하여 구현
- **힙(heap)을 이용**하여 구현할 수 있다.

## 힙(Heap)의 특징

- 힙은 **완전 이진 트리** 자료구조의 일종
  - **완전 이진 트리** : 루트(root) 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로
데이터가 차례대로 삽입되는 트리(tree)를 의미.
- 힙에서는 **항상 루트 노드(root node)를 제거**
- **최소 힙(min heap)**
  - 루트 노드가 가장 작은 값을 가짐.
  - 따라서 값이 작은 데이터가 우선적으로 제거
- **최대 힙(max heap)**
  - 루트 노드가 가장 큰 값을 가짐.
  - 따라서 값이 큰 데이터가 우선적으로 제거
- 힙의 시간복잡도
  - O(logN)
  
> <h3>heapq

+ 파이썬에서는 우선순위 큐를 heapq 라이브러리를 통해서 구현 가능하다.

``` python
# 최소 힙 구현 방법 : 우선순위가 높은 값은 제일 작은 값
import heapq

q = []
heapq.heappush(q, value)  # q 리스트에 value를 우선순위 큐(최소 힙)로 넣는다.
print(heapq.heappop(q))  # q 리스트에서 제일 작은 값(우선순위가 높은 값)을 뽑아내서 출력한다.

# 최대 힙 구현 방법 : 우선순위가 높은 값은 제일 큰 값
q = []
heapq.heappush(q, -value)  # q 리스트에 value를 우선순위 큐(최대 힙)로 넣는다.
print(-heapq.heappop(q))  # q 리스트에서 제일 큰 값(우선순위가 높은 값)을 뽑아내서 출력한다.
```
