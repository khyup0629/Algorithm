import sys
sys.setrecursionlimit(10**5)

n = int(input())

paper = []
for _ in range(n):
    array = list(map(int, input().split()))
    paper.append(array)

cnt_m1, cnt_0, cnt_1 = 0, 0, 0  # -1, 0, 1의 갯수


def dfs(n, point):
    global cnt_m1, cnt_0, cnt_1
    for x, y in point:
        changed = False
        for i in range(x, x+n):
            for j in range(y, y+n):
                if paper[i][j] != paper[x][y]:
                    changed = True
                    # 9등분 했을 때 사각형 하나의 길이
                    standard = n // 3
                    # 종이를 9등분한 시작점 기록
                    point = [(x, y), (x, y+standard), (x, y+standard * 2),
                             (x+standard, y), (x+standard, y+standard), (x+standard, y+standard * 2),
                             (x+standard * 2, y), (x+standard * 2, y+standard), (x+standard * 2, y+standard * 2)]
                    dfs(standard, point)  # 재귀 호출
                    break
            if changed:
                break
        if not changed:  # 한 사각형 안에 모든 숫자가 같으면, 해당하는 숫자 카운트 +1
            if paper[x][y] == -1:
                cnt_m1 += 1
            elif paper[x][y] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1


point = [(0, 0)]
dfs(n, point)

print(cnt_m1)
print(cnt_0)
print(cnt_1)
