# N-Queen 문제처럼 생각하면 됨. 연산자의 개수만큼 n x n 칸을 만들고
# 행을 하나씩 옮겨가면서 다른 열일 때만 계산을 허용하도록 한다.
# 백트래킹을 이용, PyPy3 제출

n = int(input())

number = list(map(int, input().split(' ')))

mark_number = list(map(int, input().split(' ')))
# 열에 대해서 방문했는지 여부가 저장될 공간
visited = [False] * (n - 1)
# 계산 중간 과정에서 중간 연산의 결과값이 저장될 공간
visited_score = [0] * n

# 연산자로 구성된 리스트를 만들어 나중에 인덱스를 활용하여 계산에 이용
mark = []
for i in range(4):
    for _ in range(mark_number[i]):
        if i == 0:
            mark.append('+')
        elif i == 1:
            mark.append('-')
        elif i == 2:
            mark.append('*')
        elif i == 3:
            mark.append('/')
# 초기값
visited_score[0] = number[0]
# 행의 끝까지 연산이 완료되었을 때 각 결과값이 저장될 공간
max_min = []


def expression(x):
    global max_min
    if x == (n - 1):
        # 끝까지 계산 되었을 때 결과값 저장
        max_min.append(visited_score[n - 1])
        return
    for y in range(n - 1):
        # 같은 열에 중복되지 않을 때
        if not visited[y]:
            visited[y] = True  # 방문 완료
            # 현재 열에 해당되는 연산자로 계산
            if mark[y] == '+':
                visited_score[x + 1] = visited_score[x] + number[x + 1]
            if mark[y] == '-':
                visited_score[x + 1] = visited_score[x] - number[x + 1]
            if mark[y] == '*':
                visited_score[x + 1] = visited_score[x] * number[x + 1]
            if mark[y] == '/':
                # 음수 / 양수일 경우 -(|음수| // 양수)를 취하라고 문제 조건에 명시
                if visited_score[x] < 0:
                    visited_score[x + 1] = -(abs(visited_score[x]) // number[x + 1])
                else:
                    visited_score[x + 1] = visited_score[x] // number[x + 1]
            expression(x + 1)
            visited_score[x + 1] = 0  # 백트래킹
            visited[y] = False  # 백트래킹


# 재귀 함수 수행
expression(0)

# 연산의 결과값 중 최대값, 최소값 출력
print(max(max_min))
print(min(max_min))

"""
문제
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 
연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 
이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 
주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 
예를 들어, 아래와 같은 식을 만들 수 있다.

1+2+3-4×5÷6
1÷2+3+4-5×6
1+2÷3×4-5+6
1÷2×3-4+5+6
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 
또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 
즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 
이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

1+2+3-4×5÷6 = 1
1÷2+3+4-5×6 = 12
1+2÷3×4-5+6 = 5
1÷2×3-4+5+6 = 7
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. 
(1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

예제 입력 1 
2
5 6
0 0 1 0
예제 출력 1 
30
30
예제 입력 2 
3
3 4 5
1 0 1 0
예제 출력 2 
35
17
예제 입력 3 
6
1 2 3 4 5 6
2 1 1 1
예제 출력 3 
54
-24
예제 입력 4
3
1 8 2
0 1 0 1
예제 출력 4
-2
-3
"""