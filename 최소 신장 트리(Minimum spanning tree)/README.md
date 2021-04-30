출처 : [한빛미디어] 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈 저)

---
# 최소 신장 트리 (Minimum spanning tree)

+ [신장 트리](#신장-트리)
+ [최소 신장 트리](#최소-신장-트리)
+ [크루스칼 알고리즘](#크루스칼-알고리즘)
	+ [1) 동작 과정](#1-동작-과정)
	+ [2) 코드 분석](#2-코드-분석)
	+ [3) 성능 분석](#3-성능-분석)

---
## 신장 트리

+ 그래프에서 **모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프**를 의미.
	+ 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 하다.
	+ **사이클이 존재하는 조건**은 서로소 집합 자료구조에서와 같이 **부모 노드가 같아진다는 것**을 의미한다.

![image](https://user-images.githubusercontent.com/43658658/116685081-c2c50580-a9ec-11eb-9b10-acef247b8693.png)

+ 어떤 그래프에서 모든 간선을 사용하지 않아도 되는 문제에 대해 적용하기 좋은 아이디어.

---
## 최소 신장 트리
+ 최소한의 비용으로 구성되는 신장 트리를 찾아야 할 때 어떻게 해야 할까?
+ 예를 들어 N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우를 생각해 보자.
	+ 두 도시 A, B를 선택했을 때 A에서 B로 이동하는 경로가 반드시 존재하도록 도로를 설치한다.

![image](https://user-images.githubusercontent.com/43658658/116685496-66aeb100-a9ed-11eb-88e7-605d98be156a.png)

+ 모든 도시를 이으면서 비용이 최소가 되는 그래프는 오른쪽과 같다.

---
## 크루스칼 알고리즘

+ 대표적인 **최소 신장 트리 알고리즘**
+ **그리디 알고리즘**으로 분류
+ 구체적인 동작 과정은 다음과 같다.
	1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
	2. 간선을 하나씩 확인하며 **현재의 간선이 사이클을 발생시키는지 확인**한다.
		1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
		2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
	3. 모든 간선에 대하여 2번의 과정을 반복

[위로](#최소-신장-트리-Minimum-spanning-tree)

### 1) 동작 과정

+ [초기 단계] 그래프의 모든 간선 정보에 대하여 오름차순 정렬 수행

![image](https://user-images.githubusercontent.com/43658658/116688007-0752a000-a9f1-11eb-8f65-7c5b19424738.png)

> union(3,4) (union 함수 이용)

+ [Step 1] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (3, 4)를 선택하여 처리한다.
	+ 신장트리 포함
	
![image](https://user-images.githubusercontent.com/43658658/116688362-9069d700-a9f1-11eb-8e19-0abe4432099c.png)

> union(4,7)

+ [Step 2] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (4, 7)를 선택하여 처리한다. 
	+ 신장트리 포함

![image](https://user-images.githubusercontent.com/43658658/116688440-abd4e200-a9f1-11eb-85f0-31137d0f4438.png)

> union(4,6)

+ [Step 3] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (4, 6)를 선택하여 처리한다. (union 함수 이용) 
	+ 신장트리 포함

![image](https://user-images.githubusercontent.com/43658658/116688465-b4c5b380-a9f1-11eb-9042-57cc5ab13fbb.png)

> *union(3,4)*

+ [Step 4] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (3, 4)를 선택하여 처리한다. (union 함수 이용) 
	+ 사이클 발생, 신장트리 미포함

![image](https://user-images.githubusercontent.com/43658658/116688552-d6269f80-a9f1-11eb-8393-f4e287ddb552.png)

> union(1,2)

+ [Step 5] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (1, 2)를 선택하여 처리한다. (union 함수 이용) 
	+ 신장트리 포함

![image](https://user-images.githubusercontent.com/43658658/116688779-23a30c80-a9f2-11eb-94b0-704004fc9eb6.png)

> union(2,6)

+ [Step 6] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (2, 6)를 선택하여 처리한다. (union 함수 이용) 
	+ 신장트리 포함

![image](https://user-images.githubusercontent.com/43658658/116688671-fce4d600-a9f1-11eb-8af7-8449cebd6079.png)

> *union(2,3)*

+ [Step 7] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (2, 3)를 선택하여 처리한다. (union 함수 이용) 
	+ 사이클 발생, 신장트리 미포함

![image](https://user-images.githubusercontent.com/43658658/116688883-4df4ca00-a9f2-11eb-84b8-30504b595c33.png)

> union(5,6)

+ [Step 8] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (5, 6)를 선택하여 처리한다. (union 함수 이용) 
	+ 신장트리 포함

![image](https://user-images.githubusercontent.com/43658658/116688828-34538280-a9f2-11eb-897a-22ee7489be6a.png)

> *union(1,5)*

+ [Step 9] 아직 처리하지 않은 간선 중에서 가장 짧은 간선인 (1, 5)를 선택하여 처리한다. (union 함수 이용) 
	+ 사이클 발생, 신장트리 미포함

![image](https://user-images.githubusercontent.com/43658658/116688931-5d741300-a9f2-11eb-8a53-734da13c0bf7.png)

+ [알고리즘 수행 결과] 최소 신장 트리에 포함되어 있는 간선의 비용만 모두 더하면, 그 값이 최종 비용에 해당한다.

![image](https://user-images.githubusercontent.com/43658658/116688962-68c73e80-a9f2-11eb-8bbe-af044de1b99c.png)

[위로](#최소-신장-트리-Minimum-spanning-tree)

### 2) 코드 분석
``` python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
```

### 3) 성능 분석

+ 크루스칼 알고리즘은 간선의 개수가 E개일 때, **O(ElogE)**의 시간 복잡도를 가진다.
+ 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선의 정렬을 수행하는 부분이다.
	+ 표준 라이브러리(sort)를 이용해 E개의 데이터를 정렬하기 위한 시간 복잡도는 O(ElogE)이다.

[위로](#최소-신장-트리-Minimum-spanning-tree)

---
