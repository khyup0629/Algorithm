T = int(input())

result_count = []
for k in range(T):
    n, m = map(int, input().split(' '))
    gold = list(map(int, input().split(' ')))

    # 금의 개수를 2차원 배열로 만들기
    graph = []
    index = 0
    for i in range(n):
        graph.append(gold[index:index+m])
        index += m
    # DP 테이블을 2차원 배열로 만듦
    d = [[0 for j in range(m)] for i in range(n)]
    # 최대값 저장소인 d의 1열에 초기값 설정
    for i in range(n):
        d[i][0] = graph[i][0]
    # DP 진행
    for i in range(1, m):
        for j in range(n):
            if (j - 1) >= 0:
                d[j][i] = max(d[j][i], d[j-1][i-1] + graph[j][i])
            d[j][i] = max(d[j][i], d[j][i-1] + graph[j][i])
            if (j + 1) < n:
                d[j][i] = max(d[j][i], d[j+1][i-1] + graph[j][i])
    # 마지막 열의 원소 중 최대값 구하기
    max_count = 0
    for i in range(n):
        max_count = max(max_count, d[i][m-1])

    result_count.append(max_count)

for k in result_count:
    print(k)

"""
입력 조건
- 첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)
- 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20)
- 둘째 줄에 n x m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다.
(1 <= 금의 개수 <= 100)

출력 조건
- 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다.
각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.

입력 예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

출력 예시
19
16
"""