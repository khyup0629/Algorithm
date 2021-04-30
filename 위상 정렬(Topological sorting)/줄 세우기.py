# 방향이 있고(키 비교), 전입차수가 낮은 순으로 정렬되어야 하므로
# 위상 정렬에 해당한다.

from collections import deque
# 학생 수, 키를 비교한 횟수
n, m = map(int, input().split())

# 전입차수 초기화
indegree = [0] * (n + 1)

# 그래프 그리기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topological_sorting():
    q = deque()
    # 전입차수가 0인 수를 q에 넣는다.
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:  # q가 빌 때까지 반복
        now = q.popleft()
        result.append(str(now))
        for i in graph[now]:
            indegree[i] -= 1  # i로 가는 전입차수 -1
            if indegree[i] == 0:
                q.append(i)


result = []
topological_sorting()

print(' '.join(result))

"""
문제
N명의 학생들을 키 순서대로 줄을 세우려고 한다. 
각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

입력
첫째 줄에 N(1≤N≤32,000), M(1≤M≤100,000)이 주어진다. M은 키를 비교한 회수이다. 
다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

학생들의 번호는 1번부터 N번이다.

출력
첫째 줄부터 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.

예제 입력 1 
3 2
1 3
2 3
예제 출력 1 
1 2 3
예제 입력 2 
4 2
4 2
3 1
예제 출력 2 
4 2 3 1
입력 예시 3
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
출력 예시 3
1 2 5 3 6 4 7
"""