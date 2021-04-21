# 문제 핵심 아이디어를 파악해야 간단히 풀 수 있는 문제
# 저울추 리스트를 오름차순 정렬하고 앞에서부터 누적해서 무게를 더한다.
# '여태까지 추의 합 + 1 >= 다음 추의 무게' 가 성립하지 않는다면
# (여태까지 추의 합 + 1)의 값이 만들 수 없는 최소 무게가 된다.

n = int(input())

data = list(map(int, input().split()))
data.sort()

result = 0
for i in data:
    if result + 1 >= i:
        result += i
    else:
        break

print(result + 1)

"""
문제
하나의 양팔 저울을 이용하여 물건의 무게를 측정하려고 한다. 
이 저울의 양 팔의 끝에는 물건이나 추를 올려놓는 접시가 달려 있고, 양팔의 길이는 같다. 
또한, 저울의 한쪽에는 저울추들만 놓을 수 있고, 다른 쪽에는 무게를 측정하려는 물건만 올려놓을 수 있다.

무게가 양의 정수인 N개의 저울추가 주어질 때, 이 추들을 사용하여 측정할 수 없는 양의 정수 무게 중 최솟값을 구하는 프로그램을 작성하시오.

예를 들어, 무게가 각각 3, 1, 6, 2, 7, 30, 1인 7개의 저울추가 주어졌을 때, 이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21이다. 

입력
첫 째 줄에는 저울추의 개수를 나타내는 양의 정수 N이 주어진다. N은 1 이상 1,000 이하이다. 
둘째 줄에는 저울추의 무게를 나타내는 N개의 양의 정수가 빈칸을 사이에 두고 주어진다. 
각 추의 무게는 1이상 1,000,000 이하이다.

출력
첫째 줄에 주어진 추들로 측정할 수 없는 양의 정수 무게 중 최솟값을 출력한다.

예제 입력 1 
7
3 1 6 2 7 30 1
예제 출력 1 
21
"""

"""
# 메모리 초과 방식
from itertools import combinations
# 저울의 개수
n = int(input())
# 저울의 종류
data = list(map(int, input().split()))

possible = []
for i in data:
    possible.append([i])

for i in range(1, n):
    for j in list(combinations(data, i+1)):
        possible.append(j)

possible_weight = []
for i in possible:
    if possible_weight.count(sum(i)) == 1:
        continue
    possible_weight.append(sum(i))

possible_weight.sort()

min_number = 0
while True:
    min_number += 1
    if possible_weight.count(min_number) != 1:
        print(min_number)
        break
"""