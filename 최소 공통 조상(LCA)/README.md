# 최소 공통 조상(Lowest Common Ancestor)

## 최소 공통 조상(Lowest Common Ancestor)

- 두 노드의 공토된 조상 중에서 가장 가까운 조상을 찾는 문제.

![image](https://user-images.githubusercontent.com/43658658/124074763-ece38400-da7e-11eb-9fad-8d602e092bbc.png)

## 최소 공통 조상 찾기 알고리즘

[참고 문제](https://www.acmicpc.net/problem/11437)

1. 모든 노드에 대한 깊이(depth)를 계산

![image](https://user-images.githubusercontent.com/43658658/124074854-0be21600-da7f-11eb-964a-f96115ed494b.png)

2. 최소 공통 조상을 찾을 두 노드 확인
	1. 먼저 두 노드의 깊이(depth)가 동일하도록 거슬러 올라간다.

  ![image](https://user-images.githubusercontent.com/43658658/124075517-f15c6c80-da7f-11eb-9573-e33d14dd95d7.png)

	2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다.
  
  ![image](https://user-images.githubusercontent.com/43658658/124075671-35e80800-da80-11eb-9988-f2091ebd8d99.png)
  
3. 모든 LCA(a, b) 연산에 대하여 2번의 과정을 반복한다.

- 매 쿼리마다 부모 방향으로 거슬러 올라가기 위해 최악의 경우 O(N)의 시간 복잡도 요구.
- 모든 쿼리를 처리할 때의 시간 복잡도는 O(NM)

## 최소 공통 조상(LCA) 알고리즘 개선하기

[참고 문제](https://www.acmicpc.net/problem/11438)

- 각 노드가 거슬러 올라가는 속도를 빠르게 만드는 방법에 대해 고민해보자.
	- 만약 총 15칸을 거슬러 올라가야 한다면
		- 8칸 -> 4칸 -> 2칸 -> 1
- 2의 제곱 형태로 거슬러 올라가도록 하던 O(logN)의 시간 복잡도를 보장할 수 있다.
- 메모리를 조금 더 사용하여 각 노드에 대하여 2^i번째 부모에 대한 정보를 기록한다.

1. 모든 노드에 대하여 깊이(depth)와 2^i번째 부모에 대한 정보를 계산한다.

![image](https://user-images.githubusercontent.com/43658658/124076129-cfafb500-da80-11eb-8471-a70e363dfce4.png)

- 13, 15번 노드의 LCA
2. 먼저 두 노드의 깊이를 맞춘다.

![image](https://user-images.githubusercontent.com/43658658/124076396-27e6b700-da81-11eb-902f-f46eacf0d06c.png)

3. 부모 노드가 같아질 때까지 2^i 꼴로 거슬러 올라간다.

![image](https://user-images.githubusercontent.com/43658658/124076644-81e77c80-da81-11eb-90fd-ab44070a9166.png)

- 다이나믹 프로그래밍(Dynamic Programming)을 이용해 시간 복잡도를 개선할 수 있다.
	- 세그먼트 트리를 이용하는 방법도 존재한다.
- 매 쿼리마다 부모를 거슬러 올라가기 위해 O(logN)의 복잡도가 필요하다.
	- 따라서 모든 쿼리를 처리할 때의 시간 복잡도는 O(MlogN)이다.
