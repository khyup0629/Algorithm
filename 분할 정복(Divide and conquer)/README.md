# 분할 정복(Divide and conquer)

## 1. 소개

> <h3>분할 정복 알고리즘의 설계 전략

+ Divide : 해결할 문제를 여러 개의 작은 부분 문제들로 분할
+ Conquer : 나눈 작은 문제를 각각 해결
+ Combine : 필요시 해결된 해답을 모음

> <h3>Top-Down 접근방식

+ 문제의 크기가 n이라면
+ Divide : 크기가 n/2인 부분문제1, 크기가 n/2인 부분문제2로 나눈다.
+ Conquer : 부분문제1의 해, 부분문제2의 해
+ Combine : 전체 문제의 해(부분문제1+부분문제2)

## 2. 거듭제곱

> <h3>반복 알고리즘 : O(n)

+ C⁴ = C X C X C X C

``` python
def iterative_power(C, n):
  result = 1
  for _ in range(n):
    result = result * C
  return result
```

> <h3>재귀 알고리즘 : O(log₂n)

+ C⁴ = (C²)² X (C²)²

``` python
def recursive_power(C, n):
	if n == 1:
		return C
	if n % 2 == 0
		y = recursive_power(C, n//2)
		return y * y
	else:
		y = recursive_power(C, (n-1)//2)
		return y * y * C
```

## 3. 병합 정렬

+ 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
+ 분할 정복 알고리즘 활용
+ 자료를 최소 단위의 문제까지 나눈 후, 차례대로 정렬하여 최종 결과 획득
+ 시간 복잡도 : O(nlogn)

> <h3>병합 정렬 과정

+ {69, 10, 30, 2, 16, 8, 31, 22}를 병합 정렬하는 과정
+ 분할 단계 - 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 계속 분할

![image](https://user-images.githubusercontent.com/43658658/118113071-c7dc7880-b420-11eb-818c-187ece5ba0ab.png)

+ 병합 단계 - 2개의 부분집합을 정렬하면서 하나의 집합으로 병합

![image](https://user-images.githubusercontent.com/43658658/118113273-0b36e700-b421-11eb-9114-a7f46f910523.png)

+ 8개의 부분집합이 1개가 될 때까지 병합

![image](https://user-images.githubusercontent.com/43658658/118113622-797ba980-b421-11eb-8eb8-7294d181bafd.png)

> <h3>병합 정렬 코드

``` python
def merge_sort(m):
	if len(m) <= 1:  # 사이즈가 0이거나 1인 경우, 바로 리턴
		return m
	# 1. Divide 부분
	mid = len(m) // 2
	left = m[:mid]
	right = m[mid:]

	# 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
	left = merge_sort(left)
	right = merge_sort(right)

	# 2. Conquer 부분 : 분할된 리스트들 병합
	return merge(left, right)

def merge(left, right):
	result = []  # 두 개의 분할된 리스트를 병합하여 result를 만듦.
	
	while len(left) > 0 and len(right) > 0:  # 양쪽 리스트에 원소가 남아있는 경우
		# 두 서브 리스트의 첫 원소들을 비교하여 작은 것부터 result에 추가
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	if len(left) > 0:  # 왼쪽 리스트에 원소가 남아있는 경우
		result.extend(left)
	if len(right) > 0:  # 오른쪽 리스트에 원소가 남아있는 경우
		result.extend(right)
	return result
```

