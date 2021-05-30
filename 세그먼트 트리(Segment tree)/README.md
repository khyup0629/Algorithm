# 세그먼트 트리(Segment tree)

+ [구간 합 구하기](#구간-합-구하기)
+ [Lazy Propagation](#Lazy-Propagation)

---
## 구간 합 구하기

+ 문제를 통해 세그먼트 트리의 개념과 구현 방법에 대해 알아보자.

> <h3>풀이 설명

[문제] => [구간 합 구하기](https://www.acmicpc.net/problem/2042)

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
        num[b-1] = c  # 업데이트
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
        num[b-1] = c  # 업데이트
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

## Lazy Propagation

[문제] => [구간 합 구하기 2](https://www.acmicpc.net/problem/10999)

+ 변경되는 원소가 '하나'가 아닌 '구간'일 경우 Lazy Propagation을 이용해야 효율적인 계산을 할 수 있다.

> <h3>update 함수의 변경

+ 기존 '구간 합 구하기' 문제에서 update 함수를 '구간이 변경'되는 특징에 맞게 약간 고쳐보았다.

``` python
def update(node, d, start, end, left, right):
    if end < left or right < start:
        return

    if start == end:
        tree[node] = num[start] + d
        num[start] += d
    else:
        mid = (start + end) // 2
        update(node*2, d, start, mid, left, right)
        update(node*2+1, d, mid+1, end, left, right)
        tree[node] = tree[node*2] + tree[node*2+1]
```

+ 얼핏 보면 효율적으로 보일 수 있으나, 전체 숫자를 업데이트 하려면 결국 트리의 모든 노드를 방문해야 하는 비효율성을 지녔다. 시간 복잡도는 노드 개수가 N일 때 O(NlogN)이다.
+ 따라서, 더 효율적인 개념을 도입해야 하는데 이 경우 적용할 수 있는 알고리즘이 Lazy Propagation이다.

> <h3>Lazy Propagation 개념

+ 기존의 update 함수가 원소가 변경될 때마다 세그먼트 트리를 갱신해줘야했던 것과 달리,
+ Lazy 값을 이용하면 Top-down 방식으로 내려오면서 변경 구간에 해당 노드가 포함되면 변경되는 값만큼 자식 노드들의 lazy에 저장해놓기만 하고 당장 모든 노드를 업데이트 하지 않아도 된다. 
+ 그 아래 노드들은 각 노드에 방문할 때 lazy 값을 통해 업데이트를 수행한다.

+ 아래 그림은 세그먼트 트리에서 3~7을 변경하는 경우에 변경해야 하는 노드를 초록색 또는 파란색으로 칠한 그림이다.

![image](https://user-images.githubusercontent.com/43658658/120108207-26cf1b00-c19f-11eb-9f01-8f8d8a3b14c3.png)

+ 파란색으로 색칠되어 있는 3-4와 5-7은 변경해야하는 구간 3-7에 포함된다. 따라서, 3-4와 5-7을 루트로하는 서브트리는 모두 3-7에 포함되게 된다. 이런 경우에는 더 이상 업데이트를 수행하지 않고, 나중에 다시 업데이트를 수행하러 그 노드에 방문했을 때, 업데이트를 진행해도 된다.
+ 이렇게 업데이트를 미룰 때 사용하는 배열이 lazy가 된다.
+ **lazy[i]**는 다음 업데이트에 i번 노드에 더해져야할 수가 저장되어 있다.
+ 3~4를 나타내는 노드의 lazy에 10이 저장되어 있다면, 3번째 수와 4번째 수에 10을 더해야 하는데, 나중에 10을 더하겠다는 의미를 가지게 되고, 5~7의 lazy에 20이 저장되어 있다면, 5, 6, 7번째 수에 20을 더해야 하지만, **지금은 더하지 않고 나중에 더하겠다**는 의미를 가지게 된다.

> <h3>Lazy Propagation 구체적인 예시 & 코드 

+ 아래의 세그먼트 트리를 통해 Lazy 개념을 학습해보자.

![image](https://user-images.githubusercontent.com/43658658/120108608-e83a6000-c1a0-11eb-8811-a0c1c121287a.png)

+ 위쪽 숫자는 각 노드가 담당하고 있는 범위, 아래 숫자는 저장되어 있는 값이다.

[step 1]

+ 여기서 3~7번째 수에 2를 더한다면, 업데이트해야하는 노드는 아래 그림과 같은 초록색과 파란색이다.

![image](https://user-images.githubusercontent.com/43658658/120108617-f38d8b80-c1a0-11eb-9954-1f21acc375d1.png)

+ **초록색 노드**는 담당하고 잇는 구간이 3~7에 **일부만 포함**되는 경우, **파란색**은 **모두 포함**되는 경우이다.
+ **초록색 노드**인 경우에는 **일반적인 세그먼트 트리를 업데이트**하는 방식으로 진행하면 되지만, **파란색 노드**의 경우에는 **조금 특별하게 진행**해야 한다.
+ 파란색 노드의 아래에 있는 노드는 모두 업데이트하려고 하는 구간 3~7에 포함된다. 따라서, **아래에 있는 노드의 업데이트**는 **나중에 필요할 때 하기로 하고**, 그 값을 **lazy[i]에 적어둔다.**
+ 초록색 노드와 파란색 노드의 코드 구현 방법은 update 함수로서 아래와 같다.

``` python
def update(node, d, start, end, left, right):
    # 현재 노드에 남아 있는 lazy 값을 tree 값에 더해주고 초기화한다.
    # update 의 update_lazy 는 새로운 lazy 값을 받기 위함이다.
    update_lazy(node, start, end)
    if end < left or right < start:  # 전혀 속하지 않으면 스킵
        return

    if left <= start and end <= right:  # 완전히 속하면,
        tree[node] += (end-start+1) * d
        if start != end:  # 리프 노드가 아니면,
            lazy[node*2] += d  # 아래의 노드는 나중에 업데이트 하기 위해 lazy에 기록해둔다.
            lazy[node*2+1] += d
    else:  # 일부만 속하면,
        mid = (start + end) // 2
        update(node*2, d, start, mid, left, right)
        update(node*2+1, d, mid+1, end, left, right)
        tree[node] = tree[node*2] + tree[node*2+1]
```

![image](https://user-images.githubusercontent.com/43658658/120108668-36e7fa00-c1a1-11eb-96ec-6c6aa8100eb3.png)

+ 노드 옆에 회색으로 적혀있는 숫자가 해당 노드의 lazy 값이다. 없는 노드의 lazy 값은 0이다.
+ 앞으로는 항상 어떤 노드를 방문할 때마다 lazy 값이 있는지를 검사해야 한다. **만약에, lazy 값이 0이 아니라면**, **현재 노드에 해당하는 값을 올바르게 더해주고, 자식 노드에게 lazy를 물려줘야 한다.** 여기서 **올바르게란, 단순히 lazy[i]의 값을 더하는 것이 아니고, lazy[i]의 값에 end-start+1의 값을 곱해서 더하는 것을 의미**한다. 해당하는 노드가 담당하는 구간이 start ~ end라면, **총 담당하는 수의 개수는 end-start+1개** 이기 때문에, 곱해서 더해주어야 한다.
+ 위의 알고리즘을 함수로 표현하면 아래와 같은 코드로 작성된다.

``` python
def update_lazy(node, start, end):  # 현재 노드에 남아있는 lazy 값을 tree 값에 더해준다.
    if lazy[node] != 0:
        tree[node] += (end-start+1) * lazy[node]  # 올바르게 더해준다.
        if start != end:  # 리프 노드가 아니면,
            lazy[node*2] += lazy[node]  # 자식 노드에게 lazy 값을 물려준다.
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0  # 초기화
```

[step 2]

+ 이제 4~9번째 수에 1을 더해보자.

![image](https://user-images.githubusercontent.com/43658658/120108901-19fff680-c1a2-11eb-9ae0-1326fd8ac3e6.png)

+ 실제로는 3~4에서 3번과 4번을 담당하는 노드를 호출하기 때문에, 3번만 담당하는 노드도 호출하게 된다.

![image](https://user-images.githubusercontent.com/43658658/120108923-369c2e80-c1a2-11eb-9b0c-41cc04867014.png)

+ 3번과 4를 담당하는 노드에 방문했을 때는, lazy값이 0보다 크기 때문에, lazy값을 먼저 업데이트해주고나서 1을 더해주게 된다. (이는 후에 update, base_case_sum 함수의 첫 부분에 update_lazy 함수를 넣음으로써 구현할 수 있다. update_lazy 함수를 통해 해당 노드의 lazy 값을 업데이트 해주고 초기화해준 뒤에 update를 통해 1을 더해주는 것이다.) 따라서, 트리에 저장되어 있는 값과 lazy 값은 아래 그림과 같게 된다.

![image](https://user-images.githubusercontent.com/43658658/120109051-ba561b00-c1a2-11eb-950e-d83c641a04e0.png)

[step 3]

+ 마지막으로 6에서 8까지 합을 구하는 과정을 살펴보자.
+ 6에서 8의 합을 구하려면 아래 그림에서 초록색으로 색칠되어 있는 정점을 방문해야 한다.

![image](https://user-images.githubusercontent.com/43658658/120109117-0903b500-c1a3-11eb-90b5-c2fc38261c83.png)

+ 루트 노드의 0~9 구간은 더해야 하는 구간인 6~8 구간과 겹치기 때문에, 좌우 자식 노드인 0~4와 5~9를 호출한다.
+ 0~4는 6~8과 전혀 겹치지 않기 때문에 0을 리턴한다.
+ 5~9는 6~8과 겹치기 때문에 좌우 자식 노드인 5~7과 8~9를 호출한다.
+ 5~7 노드는 lazy 값을 가지고 있다. update_lazy를 통해 현재 노드를 업데이트하고, 자식에게 lazy 값인 1을 물려준다.
+ 5~7에 저장되어 있는 값은 24이고, lazy의 값은 1이기 때문에, 5~7에 저장될 값은 24 + 1*(7-5+1) = 27이 된다. 이제 자식들에게 lazy 값을 물려주기 때문에, 자식들의 lazy 값은 모두 1이 더해져 3이 된다.

![image](https://user-images.githubusercontent.com/43658658/120109283-af4fba80-c1a3-11eb-8342-399c4622a443.png)

+ 5~7은 6~8과 겹치기 때문에, 자식 5~6과 7을 호출하게 된다.
+ 5~6에는 lazy값이 있기 때문에, 현재 노드를 업데이트하고, 자식에게 lazy 값을 물려준다.

![image](https://user-images.githubusercontent.com/43658658/120109332-f0e06580-c1a3-11eb-8a84-304beecfcdc9.png)

+ 5~6도 6~8과 겹치기 때문에, 자식 5와 6을 호출하게 된다.
+ 자식 5와 6은 합쳐서 설명한다. 5와 6은 모두 lazy 값이 있기 때문에, 노드를 업데이트한다. 각각 3이 더해져 5는 4, 6은 11이 된다. 자식은 없기 때문에, lazy를 물려줄 수 없다. 5는 6~8에 포함되지 않기 때문에 0을 리턴하고, 6은 6~8에 포함되기 때문에, 저장되어 있는 값을 리턴한다.

![image](https://user-images.githubusercontent.com/43658658/120109393-3735c480-c1a4-11eb-9853-59f453fff9e9.png)

+ 7번 노드는 lazy값이 있기 때문에, 먼저 노드를 업데이트한다. 6~8에 7은 포함되기 때문에, 저장되어 있는 값을 리턴한다.

![image](https://user-images.githubusercontent.com/43658658/120109427-63e9dc00-c1a4-11eb-9996-6b23b7e90d23.png)

+ 이제 8~9번 노드를 방문한다. 역시 lazy 값이 있기 때문에, 노드를 업데이트하고, 자식에게 lazy 값을 물려주게 된다. 그 다음, 8~9는 6~8과 겹치기 때문에, 두 자식을 각각 호출해야 한다.

![image](https://user-images.githubusercontent.com/43658658/120109454-81b74100-c1a4-11eb-9f02-f0f0b1967a99.png)

+ 8번과 9번노드도 함께 설명한다. 두 노드 모두 lazy가 있기 때문에, 노드를 업데이트한다. 8은 6~8에 포함되기 때문에 저장되어 있는 값을 리턴하고, 9는 포함되지 않기 때문에 0을 리턴한다.

![image](https://user-images.githubusercontent.com/43658658/120109473-91cf2080-c1a4-11eb-8828-b56c0dd9acb2.png)

+ 마지막으로 **리턴한 값들을 모두 더하면서 재귀적으로 거슬러 올라가면** 원하는 답을 얻을 수 있다.
+ step 3를 base_case_sum 함수로 표현하면 아래와 같다. 일반적인 세그먼트 트리의 합 구하기와 같으나 **update_lazy를 초반에 적어줌으로써 lazy 값을 tree에 업데이트한다는 것이 차이점**이다.

 ``` python
 def base_case_sum(node, start, end, left, right):
    # 현재 노드에 남아 있는 lazy 값을 tree 값에 더해주고 이를 합에 반영하기 위함으로 update_lazy 를 쓴다.
    update_lazy(node, start, end)
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return base_case_sum(node*2, start, mid, left, right) + base_case_sum(node*2+1, mid+1, end, left, right)
```

+ 이 문제의 전체 코드는 아래와 같다.

``` python
# 변경되는 원소가 하나가 아닌 '구간' 일 경우 Lazy Propagation 을 이용한다.
from math import *
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, k = map(int, input().split())

h = int(ceil(log2(n)))
t_size = 1 << (h+1)
tree = [0] * t_size
lazy = [0] * t_size  # lazy 값.

num = [int(input()) for _ in range(n)]


def init(node, start, end):
    if start == end:
        tree[node] = num[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]


def update_lazy(node, start, end):  # 현재 노드에 남아있는 lazy 값을 tree 값에 더해준다.
    if lazy[node] != 0:
        tree[node] += (end-start+1) * lazy[node]
        if start != end:  # 리프 노드가 아니면,
            lazy[node*2] += lazy[node]  # 자식 노드에게 lazy 값을 물려준다.
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0  # 초기화


def update(node, d, start, end, left, right):
    # 현재 노드에 남아 있는 lazy 값을 tree 값에 더해주고 초기화한다.
    # update 의 update_lazy 는 새로운 lazy 값을 받기 위함이다.
    update_lazy(node, start, end)
    if end < left or right < start:  # 전혀 속하지 않으면 스킵
        return

    if left <= start and end <= right:  # 완전히 속하면,
        tree[node] += (end-start+1) * d
        if start != end:  # 리프 노드가 아니면,
            lazy[node*2] += d  # 아래의 노드는 나중에 업데이트 하기 위해 lazy에 기록해둔다.
            lazy[node*2+1] += d
    else:  # 일부만 속하면,
        mid = (start + end) // 2
        update(node*2, d, start, mid, left, right)
        update(node*2+1, d, mid+1, end, left, right)
        tree[node] = tree[node*2] + tree[node*2+1]


def base_case_sum(node, start, end, left, right):
    # 현재 노드에 남아 있는 lazy 값을 tree 값에 더해주고 이를 합에 반영하기 위함으로 update_lazy 를 쓴다.
    update_lazy(node, start, end)
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return base_case_sum(node*2, start, mid, left, right) + base_case_sum(node*2+1, mid+1, end, left, right)


init(1, 0, n-1)

for _ in range(m+k):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        update(1, arr[3], 0, n-1, arr[1]-1, arr[2]-1)
    else:
        print(base_case_sum(1, 0, n-1, arr[1]-1, arr[2]-1))

```





