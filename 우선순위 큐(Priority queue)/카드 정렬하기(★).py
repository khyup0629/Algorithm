# 문제 풀이 아이디어
# 1. 우선순위 큐를 두고 입력값을 모두 넣는다.
# 2. 우선순위 큐에서 가장 작은 수 두 개를 뽑아내고 더한다
# 3. 우선순위 큐에 더한 값을 넣는다.
# 4. 2~3의 과정을 반복하며 더한 값을 모두 더한다.
import heapq
import sys
input = sys.stdin.readline

n = int(input())

group = []
for _ in range(n):
    heapq.heappush(group, int(input()))

result = 0
left, right = 0, 0  # 더할 두 수
while group:
    num = heapq.heappop(group)
    if left == 0:  # 왼쪽 값이 없다면 왼쪽 값에 추가
        left = num
    elif right == 0:  # 오른쪽 값이 없다면
        right = num  # 오른쪽 값 추가
        s = left + right  # 두 수를 더해준다.
        result += s  # 더한 값(s)을 모두 더한다.
        heapq.heappush(group, s)  # 우선순위 큐에 더한 값(s)을 넣는다.
        left, right = 0, 0  # 더할 두수 초기화

print(result)

# 문제 : https://www.acmicpc.net/problem/1715
