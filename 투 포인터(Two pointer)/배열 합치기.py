# 계산시간이 다른 코드에 비해 빨랐다.
# 코드는 좀 더 길어졌으나 계산 시간과 메모리 면에서 성능이 좋았다.
n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

point_a, point_b = 0, 0

result = []
# 어느 한쪽 배열의 끝에 다다르면 반복 종료
while point_a < n and point_b < m:
    if a[point_a] >= b[point_b]:
        result.append(str(b[point_b]))
        point_b += 1
    else:
        result.append(str(a[point_a]))
        point_a += 1

# 남아 있는 수열을 모두 result에 넣어준다.
if point_a == n:
    for i in range(point_b, m):
        result.append(str(b[i]))
else:
    for i in range(point_a, n):
        result.append(str(a[i]))

"""
result = []
while point_a < n or point_b < m:
    # point_b < m 에서 False가 나면 뒤의 조건은 보지 않고 바로 전체 조건이 False가 된다.
    if point_a == n or (point_b < m and a[point_a] >= b[point_b]):
        result.append(str(b[point_b]))
        point_b += 1
    elif point_b == m or (point_a < n and a[point_a] < b[point_b]):
        result.append(str(a[point_a]))
        point_a += 1
"""
print(' '.join(result))

"""
문제
정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

출력
첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.

예제 입력 1 
2 2
3 5
2 9
예제 출력 1 
2 3 5 9
예제 입력 2 
2 1
4 7
1
예제 출력 2 
1 4 7
예제 입력 3 
4 3
2 3 5 9
1 4 7
예제 출력 3 
1 2 3 4 5 7 9
예제 입력 4
3 5
6 7 8
1 2 3 4 5
예제 출력 4
1 2 3 4 5 6 7 8
예제 입력 5
3 5
5 6 7
4 5 6 7 8
예제 출력 5
4 5 5 6 6 7 7 8
"""