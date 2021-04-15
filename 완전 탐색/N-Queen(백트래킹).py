# PyPy3
n = int(input())

result = 0
# col : 열, diagonal_1 : 대각선 /, diagonal_2 : 대각선 \, 인덱스를 가리킴.
# 대각선 인덱스 총 수는 (2n-1)개
# False : 놓을 수 있음, True : 놓을 수 없음.
col, diagonal_1, diagonal_2 = [False] * n, [False] * (2*n-1), [False] * (2*n-1)

# 퀸이 무조건 한 행에 하나씩 들어가야 된다는 것을 이용
def queen(x):
    global result
    # 마지막 n행에 퀸을 놓을 수 있으면 재귀 함수를 거쳐 x = n이 된다.
    # 마지막 n행에 퀸을 놓았단 뜻은 n개의 퀸을 모두 놓았다는 것을 의미
    if x == n:
        # 퀸을 놓는 방법의 수 +1
        result += 1
        return
    # 이번 행(x)을 고정하고 열(y)을 0~n까지 움직이며 한 칸씩 탐색
    for y in range(n):
        # x : 행, y : 열
        # 같은 대각선 / 의 인덱스 x, y의 (x+y)는 일정하다
        # 같은 대각선 \ 의 인덱스 x, y의 (x-y+n-1)는 일정하다
        # 문제 풀이 아이디어 사진 참고
        if not (col[y] or diagonal_1[x+y] or diagonal_2[x-y+n-1]):
            col[y] = diagonal_1[x + y] = diagonal_2[x - y + n - 1] = True
            # 이번 행에 퀸을 놓았으면(True) 다음 행(x+1)으로 넘어가기
            queen(x+1)
            col[y] = diagonal_1[x + y] = diagonal_2[x - y + n - 1] = False  # 백트래킹


queen(0)
print(result)

"""
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92
"""
