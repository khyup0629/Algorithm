

---
# 투 포인터 (Two pointer)

+ **리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리**하는 알고리즘
+ 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 **시작점**과 **끝점** 2개의 점으로 접근할 데이터의 범위를 표현할 수 있다.

## 특정한 합을 가지는 부분 연속 수열 찾기

+ N개의 자연수로 구성된 수열이 있다.
+ **합이 M인 부분 연속 수열의 개수**를 구해보자.
+ 수행 시간 제한은 **O(N)** 이다.

![image](https://user-images.githubusercontent.com/43658658/116770909-16356300-aa82-11eb-80b8-69d484bf136b.png)

+ 완전 탐색을 수행할 경우 **O(N^2)** 만큼의 수행 시간이 요구되기에 적절하지 않다.

### 투 포인터를 활용한 문제 해결 아이디어

1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
2. 현재 부분 합이 M과 같다면, 카운트한다.
3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다. (부분 합 증가)
4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다. (부분 합 감소)
5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.

+ [초기 단계] 시작점과 끝점이 첫 번째 원소의 인덱스를 가리키도록 한다.
	+ 현재의 부분합은 1이므로 무시한다.
	+ 현재 카운트 : 0
	+ M = 5

![image](https://user-images.githubusercontent.com/43658658/116771021-11bd7a00-aa83-11eb-8c2b-d7b507c11e40.png)

+ [Step 1] 이전 단계에서 부분 합이 1이었기 때문에 end를 1 증가시킨다.
	+ 현재 부분 합: 3, 무시한다.
	+ 현재 카운트 : 0

![image](https://user-images.githubusercontent.com/43658658/116771069-6fea5d00-aa83-11eb-99f4-7c2019d51b97.png)

+ [Step 2] 이전 단계에서 부분 합이 3이었기 때문에 end를 1 증가시킨다.
	+ 현재 부분 합: 6, 무시한다.
	+ 현재 카운트 : 0

![image](https://user-images.githubusercontent.com/43658658/116771075-7b3d8880-aa83-11eb-9799-f9949de487c0.png)

+ [Step 3] 이전 단계에서 부분 합이 6이었기 때문에 start를 1 증가시킨다.
  + 현재 부분 합 : 5, 카운트를 1 증가시킨다.
  + 현재 카운트 : 1

![image](https://user-images.githubusercontent.com/43658658/116771091-a922cd00-aa83-11eb-9d6a-3d61de616989.png)

+ [Step 4] 이전 단계에서 부분 합이 5였기 때문에 start를 1 증가시킨다.
  + 현재 부분 합 : 3, 무시한다.
  + 현재 카운트 : 1

![image](https://user-images.githubusercontent.com/43658658/116771081-94ded000-aa83-11eb-8a83-a38ae6c510ec.png)

+ [Step 5] 이전 단계에서 부분 합이 3이었기 때문에 end를 1 증가시킨다.
  + 현재 부분 합 : 5, 카운트를 1 증가시킨다.
  + 현재 카운트 : 2

![image](https://user-images.githubusercontent.com/43658658/116771125-f3a44980-aa83-11eb-9621-601b6c97e6be.png)

+ [Step 6] 이전 단계에서 부분 합이 5였기 때문에 start를 1 증가시킨다.
  + 현재 부분 합 : 2, 무시한다.
  + 현재 카운트 : 2

![image](https://user-images.githubusercontent.com/43658658/116771147-120a4500-aa84-11eb-9de0-c61604ed83a4.png)

+ [Step 7] 이전 단계에서 부분 합이 2였기 때문에 end를 1 증가시킨다.
  + 현재 부분 합 : 7, 무시한다.
  + 현재 카운트 : 2

![image](https://user-images.githubusercontent.com/43658658/116771168-3ebe5c80-aa84-11eb-8ede-487c920941b3.png)

+ [Step 8] 이전 단게에서 부분 합이 7이었기 때문에 start를 1 증가시킨다.
  + 현재 부분 합 : 5, 카운트를 1 증가시킨다.
  + 현재 카운트 : 3

![image](https://user-images.githubusercontent.com/43658658/116771179-5dbcee80-aa84-11eb-8440-b2af30547691.png)

+ [알고리즘 결과] 연속 부분 수열의 합이 5인 개수는 총 **3개**이다.

### 코드 분석
``` python
n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
```

[위로](#투-포인터-Two-pointer)

---
