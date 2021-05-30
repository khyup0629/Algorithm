# 세그먼트 트리(Segment tree)

## 구간 합 구하기

+ 문제를 통해 세그먼트 트리의 개념과 구현 방법에 대해 알아보자.

> <h3>풀이 설명

[문제]
=> https://www.acmicpc.net/problem/2042

![image](https://user-images.githubusercontent.com/43658658/120097141-d7bac300-c169-11eb-9df2-94d9407416bd.png)

[Top-Down]
1. 분할 정복을 통해 숫자 배열 리스트를 나눈다.
2. 각 구간의 합을 구한다.(build 연산)
3. 구간들을 일종의 노드라고 생각하고 트리를 그린다.(Full Binary Tree가 나타난다.)
  + 만약, Full Binary Tree가 나타나지 않는 리스트 개수라면 나머지 원소들을 결괏값에 영향을 주지 않는 빈 원소로 채워준다.
  + 즉, 2의 거듭제곱 개수로 세그먼트 트리의 노드 개수를 맞춰준다.
4. 1번 쿼리(업데이트)가 들어오면 부모 노드를 따라 거슬로 올라가면서 노드들을 갱신해준다.
  + 트리의 레벨을 n이라고 하면 시간 복잡도는 **O(logN)**
5. 2번 쿼리(구간 합)가 들어오면 최상단 루트 노드부터 내려가면서 어떤 노드가 합을 구하려는 구간에 온전히 포함되면 더이상 내려가지 않고, 걸친다면 아래로 한 번 더 내려가서 더이상 내려가지 않을 때의 노드를 합한다.
  + 2번 쿼리 역시 시간 복잡도는 **O(logN)**

> <h3>전체 코드
  
``` python
from math import *
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, k = map(int, input().split())

h = int(ceil(log2(n)))  # ceil : 소숫점 자리 올림(math 함수)
cnt = 2 ** h  # 2의 거듭제곱 개수로 맞춰준다.
t_size = 1 << (h+1)  # 트리의 노드 개수
tree = [0] * t_size  # 트리의 노드 번호는 반드시 1 ~ t_size - 1

# 비어있는 칸은 0으로 합을 계산할 때 영향을 주지 않도록 한다.
num = [int(input()) for _ in range(n)]
for i in range(n, cnt):
    num.append(0)


def init(node, start, end):  # build 연산

    if start == end:  # 길이가 1인 구간일 때 tree 값을 기록. 이후로 재귀적으로 거슬러 올라가며 합을 기록.
        tree[node] = num[start]
        return tree[node]

    mid = (start + end) // 2
    # 자식 노드의 합을 부모 노드에 기록
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid+1, end)
    return tree[node]


def update(node, i, diff, start, end):  # 업데이트
    if not start <= i <= end:  # 업데이트 할 원소가 구간에 속하지 않으면 스킵.
        return

    tree[node] += diff  # 업데이트 될 값과 원래 값의 차이만큼 노드 값에 더해준다.

    if start == end:  # 길이 1 구간이면 스킵
        return
    else:  # 길이가 1보다 큰 구간이면 왼쪽, 오른쪽 구간으로 나눠서 진행.
        mid = (start + end) // 2
        update(node * 2, i, diff, start, mid)
        update(node * 2 + 1, i, diff, mid+1, end)


def base_case_sum(node, start, end, left, right):  # base-case 의 합
    if left <= start and end <= right:  # 노드가 b ~ c 구간에 완전히 속해 있는 경우 tree의 값을 반환하고 내려가는 것을 멈춘다.
        return tree[node]

    if end < left or right < start:  # 노드가 b ~ c 구간을 벗어난 경우 0의 값을 반환하고 내려가는 것을 멈춘다.
        return 0

    mid = (start + end) // 2
    # base-case 를 모두 더한다.
    return base_case_sum(node * 2, start, mid, left, right) + base_case_sum(node*2+1, mid+1, end, left, right)


init(1, 0, cnt-1)

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - num[b-1]  # 업데이트 할 값과 원래 값의 차이
        num[b-1] = c  # 업데이트(굳이 할 필요는 없다)
        update(1, b-1, diff, 0, cnt-1)  # 최상단 노드부터 시작.
    else:
        print(base_case_sum(1, 0, cnt-1, b-1, c-1))
```

> <h3>코드 구현 설명

[Full Binary Tree]
+ Full Binary Tree가 나타나지 않는 리스트 개수라면 나머지 원소들을 결괏값에 영향을 주지 않는 빈 원소로 채워준다.
+ 즉, 2의 거듭제곱 개수로 세그먼트 트리의 노드 개수를 맞춰준다.

``` python
h = int(ceil(log2(n)))  # ceil : 소숫점 자리 올림(math 함수)
cnt = 2 ** h  # 2의 거듭제곱 개수로 맞춰준다.
t_size = 1 << (h+1)  # 트리의 노드 개수
tree = [0] * t_size  # 트리의 노드 번호는 반드시 1 ~ t_size - 1

# 비어있는 칸은 0으로 합을 계산할 때 영향을 주지 않도록 한다.
num = [int(input()) for _ in range(n)]
for i in range(n, cnt):
    num.append(0)
```

![image](https://user-images.githubusercontent.com/43658658/120097345-ec4b8b00-c16a-11eb-8225-e5f633c7ffaa.png)

+ Full Binary Tree에서는 최상단 노드부터 1번 노드, 왼쪽 자식은 2번, 오른쪽 자식은 3번 노드, 다시 2번 노드의 왼쪽 자식은 4번, 오른쪽 자식은 5번 노드의 식으로 이름을 붙이면
+ 어떤 노드 n의 왼쪽 자식은 2n, 오른쪽 자식은 2n+1이 된다.
+ 이 원리를 이용하면 트리를 배열로 구현할 수 있다.

[Build 연산]
+ 세그먼트 트리의 각 구간의 노드 번호와 합을 기록한다.(세그먼트 트리의 초기값)
+ 리프 노드부터 역순으로 구간 합을 채워나간다.
+ 하나의 레벨을 다 채우면 한 단계 위 레벨은 아래 레벨의 두 자식 노드의 합을 넣어주면 된다.
 
![image](https://user-images.githubusercontent.com/43658658/120097416-4a786e00-c16b-11eb-8ea8-b34356cd8a05.png)

``` python
def init(node, start, end):  # build 연산

    if start == end:  # 길이가 1인 구간일 때 tree 값을 기록. 이후로 재귀적으로 거슬러 올라가며 합을 기록.
        tree[node] = num[start]
        return tree[node]

    mid = (start + end) // 2
    # 자식 노드의 합을 부모 노드에 기록
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid+1, end)
    return tree[node]

init(1, 0, cnt-1)
```

[Update]

+ 최상단 노드부터 아래로 내려오면서 업데이트 할 원소가 구간에 속하는 경우 그 차이만큼 더해주며 업데이트 해준다.

![image](https://user-images.githubusercontent.com/43658658/120097489-ae9b3200-c16b-11eb-862a-88999796d798.png)

``` python
def update(node, i, diff, start, end):  # 업데이트
    if not start <= i <= end:  # 업데이트 할 원소가 구간에 속하지 않으면 스킵.
        return

    tree[node] += diff  # 업데이트 될 값과 원래 값의 차이만큼 노드 값에 더해준다.

    if start == end:  # 길이 1 구간이면 스킵
        return
    else:  # 길이가 1보다 큰 구간이면 왼쪽, 오른쪽 구간으로 나눠서 진행.
        mid = (start + end) // 2
        update(node * 2, i, diff, start, mid)
        update(node * 2 + 1, i, diff, mid+1, end)
```

``` python
for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - num[b-1]  # 업데이트 할 값과 원래 값의 차이
        num[b-1] = c  # 업데이트(굳이 할 필요는 없다)
        update(1, b-1, diff, 0, cnt-1)  # 최상단 노드부터 시작.
    else:
        print(base_case_sum(1, 0, cnt-1, b-1, c-1))
```

[Sum 연산]
+ a == 2가 들어왔을 경우 b~c 구간의 합을 구해야 한다.
+ 어떤 구간이 가지는 인자 값은 (노드 번호n, 구간 시작start, 구간 끝end, b-1, c-1)을 갖는다.
+ 이를 재귀적으로 구한다. 예를 들어 부모가 (n, start, end, b-1, c-1)이라면 mid = (start+end) // 2 를 통해 2구간으로 나누고,
+ 왼쪽 자식 노드는 (2n, start, mid, b-1, c-1) 오른쪽 자식 노드는 (2n+1, mid+1, end, b-1, c-1)이 된다.
+ start ~ end 구간이 b ~ c 구간에 속하게 되면 그때의 tree 값을 반환한다.
+ start ~ end 구간이 b ~ c 구간을 아예 벗어나있는 경우는 0 값을 반환한다.
+ start ~ end 구간이 b ~ c 구간을 걸쳐 있는 경우 왼쪽, 오른쪽 구간을 나눠서 진행한다.

+ 최상단 노드부터 아래로 가면서 base-case를 구하고
+ base-case들의 return 값을 아래에서부터 재귀적으로 더하면서 올라오면 답을 구할 수 있다.

![image](https://user-images.githubusercontent.com/43658658/120097872-c8d60f80-c16d-11eb-96c4-1cedc3dca2d4.png)

``` python
def base_case_sum(node, start, end, left, right):
    if left <= start and end <= right:  # 노드가 b ~ c 구간에 완전히 속해 있는 경우 tree의 값을 반환하고 내려가는 것을 멈춘다.
        return tree[node]

    if end < left or right < start:  # 노드가 b ~ c 구간을 벗어난 경우 0의 값을 반환하고 내려가는 것을 멈춘다.
        return 0

    mid = (start + end) // 2
    # base-case를 모두 더한다.
    return base_case_sum(node * 2, start, mid, left, right) + base_case_sum(node*2+1, mid+1, end, left, right)
```
