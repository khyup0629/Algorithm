

---
# 누적 합(Prefix Sum)

+ 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것.

## 구간 합 문제

+ 연속적으로 나열된 N개의 수가 있을 때 **특정 구간의 모든 수를 합한 값을 계산**하는 문제.
+ 수열 {10, 20, 30, 40, 50}이 있다고 하자.
	+ 두 번째 수부터 네 번째수까지의 합은 20 + 30 + 40 = 90

### 문제 설명

+ N개의 정수로 구성된 수열이 있다.
+ M개의 쿼리 정보가 주어진다.
	+ 각 쿼리는 Left, Right으로 구성된다.
	+ 각 쿼리에 대하여 [Left, Right] 구간에 포함된 데이터들의 합을 출력해야 한다.
+ 수행 시간 제한은 **O(N + M)** 이다.

### 문제 해결 아이디어

+ **누적 합**을 활용한 알고리즘으로 해결하면 된다.

1. N개의 수 위치 각각에 대하여 누적 합을 계산하여 P에 저장한다.
2. 매 M개의 쿼리 정보를 확인할 때 구간 합은 P[Right] - P[Left - 1]이다.

![image](https://user-images.githubusercontent.com/43658658/116772360-6b28a780-aa89-11eb-828e-b8d12c931d51.png)

### 코드 분석
``` python
# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산 (세 번째 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
```

[위로](#누적-합Prefix-Sum)

---
