# k번째 수는 k보다 작거나 같은 수가 k개 있다는 뜻이다.
# A[i][j] = i x j 배열은 행마다 1의 배수, 2의 배수, 3의 배수, ... 로 이루어져있기 때문에
# 어떤 수 mid 보다 작은 수의 개수는 mid // i (i = 1, 2, 3, ...) 이 된다.
# 근데 n x n 행렬의 범위가 정해져있으므로 mid // i > n 보다 크다면 n이 mid 보다 작은 수의 개수가 된다.
# 입력값의 범위가 넓기 때문에 O(N^2)의 시간 복잡도로는 해결이 불가능하므로
# 이진 탐색을 이용한다. 시작 범위는 1~k이다. B[k]는 k보다 작거나 같으므로 시작 탐색 범위를 1~k로 설정해도 무방하다.

n = int(input())
k = int(input())
start, end = 1, k
result = 0

while start <= end:
    mid = (start + end) // 2
    # i번째 행렬에서 mid 보다 작은 수의 개수
    temp = 0
    for i in range(1, n+1):
        temp += min(mid//i, n)
    # k개와 '같은' 조건이 아니라 '이상' 조건으로 설정한 이유는
    # B[k]와 같은 수가 여러개 있을 경우 mid 보다 작은 수의 개수는 k를 넘어갈 수 있다.
    if temp >= k:
        result = mid  # 이때의 값을 저장
        end = mid - 1
    else:
        start = mid + 1

print(result)
