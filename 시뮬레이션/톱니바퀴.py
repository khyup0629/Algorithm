# 문제 풀이 아이디어
# 1. 임시 저장소를 두어 회전된 톱니의 번호들을 기록할 수 있도록 한다.
# N/S극을 비교할 때 영향을 받지 않도록 하기 위함이다.
# 2. dfs로 4개의 톱니를 탐색하게 한다.
# 3. 시계방향 구현 : 문자열의 오른쪽 끝 숫자 + 인덱스 0~6
#    반시계방향 구현 : 인덱스 1~7 + 문자열의 왼쪽 끝 숫자
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

w = [0] + [input().strip() for _ in range(4)]


def move(num, dir):  # 회전
    if dir == 1:  # 시계방향 구현 : 문자열의 오른쪽 끝 숫자 + 인덱스 0~6
        temp_w[num] = w[num][7] + w[num][:7]
    else:  # 반시계방향 구현 : 인덱스 1~7 + 문자열의 왼쪽 끝 숫자
        temp_w[num] = w[num][1:8] + w[num][0]


def dfs(n, dir):
    visited[n] = True
    move(n, dir)
    left = n - 1  # 현재 번호에서 왼쪽 톱니
    right = n + 1  # 현재 번호에서 오른쪽 톱니
    if left != 0 and not visited[left]:
        if w[left][2] != w[n][6]:
            dfs(left, -dir)  # 반대 방향으로 회전
    if right != 5 and not visited[right]:
        if w[n][2] != w[right][6]:
            dfs(right, -dir)  # 반대 방향으로 회전


k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    visited = [False] * 5
    temp_w = [w[i] for i in range(5)]  # 임시 톱니 저장소
    dfs(num, dir)
    w = [temp_w[i] for i in range(5)]  # 회전된 톱니들을 현재 상태로 한다.

print(int(w[1][0]) * 1 + int(w[2][0]) * 2 + int(w[3][0]) * 4 + int(w[4][0]) * 8)

# 문제 : https://www.acmicpc.net/problem/14891
