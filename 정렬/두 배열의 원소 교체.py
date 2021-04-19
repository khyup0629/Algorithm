# n : 배열 당 원소의 개수, k : 바꿔치기 최대 횟수
n, k = map(int, input().split(' '))

array_A = list(map(int, input().split(' ')))
array_B = list(map(int, input().split(' ')))
# 배열A 는 오름차순 정렬
array_A.sort()
# 배열B 는 내림차순 정렬
array_B.sort()
array_B.reverse()

for i in range(k):
    # 배열A 의 값보다 배열B 의 값이 더 크다면 둘 사이 값을 스왑
    if array_A[i] < array_B[i]:
        array_A[i], array_B[i] = array_B[i], array_A[i]
    else:  # 값을 바꿀 필요가 없으므로 반복문 종료
        break

print(sum(array_A))

"""
문제
최대 K번의 바꿔치기를 통해 배열A 의 합이 최대가 되도록 만들어라.

입력 조건
(1 <= N <= 100,000) (0 <= K <= N)
모든 원소는 10,000,000보다 작은 자연수
출력 조건
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소 합의 최댓값 출력

예제 입력 1
5 3
1 2 5 4 3
5 5 6 6 5
예제 출력 1
26
"""