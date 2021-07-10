n = int(input())

m = int(input())
broken = []
if m != 0:  # 고장난 수가 있을 때만 입력을 받는다.
    broken = list(map(int, input().split()))

start = 100
_min = abs(n - start)  # (+), (-)버튼만 눌렀을 때가 최솟값의 기준
cnt = 0
w = -1
while _min > w:  # 위아래 증감(w)이 100에서 + 또는 -버튼만 누른 횟수와 같아지면 반복 종료.
    w += 1
    # 기준 수(n) 아래쪽으로 -1 구간
    if n - w >= 0:
        changed = False  # 하나라도 고장난 수가 아니다
        for i in str(n-w):
            if int(i) in broken:
                changed = True  # 하나라도 고장난 수다
                break
        cnt = len(str(n - w)) + w
        if not changed:  # 하나라도 고장난 수가 아니면
            break  # 반복 종료
    # 기준 수(n) 위쪽으로 +1 구간
    changed = False
    for i in str(n+w):
        if int(i) in broken:
            changed = True
            break
    cnt = len(str(n+w)) + w
    if not changed:
        break

print(min(_min, cnt))

# 문제 : https://www.acmicpc.net/problem/1107
