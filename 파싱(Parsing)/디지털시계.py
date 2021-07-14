# 시계 정수를 그대로 두면 계산이 복잡해진다.
# 결국 시(hh)와 분(mm)은 초(ss)를 묶음으로 나타낸 것이므로 모두 초 단위로 바꿔서 계산한다.
def clock_integer(start, end):
    global cnt
    for i in range(start, end):
        hh = str(i // 3600)
        mm = str((i % 3600) // 60)
        ss = str((i % 3600) % 60)
        hhmmss = int(hh + mm + ss)
        if hhmmss % 3 == 0:
            cnt += 1


for _ in range(3):
    start, end = input().split()
    start = start.split(':')
    end = end.split(':')
    start_sec = 3600 * int(start[0]) + 60 * int(start[1]) + int(start[2])  # 시작 시간 초 단위
    end_sec = 3600 * int(end[0]) + 60 * int(end[1]) + int(end[2])  # 끝 시간 초 단위
    cnt = 0  # 3의 배수 개수
    if start_sec > end_sec:  # 시작 시간이 끝 시간보다 크면,
        clock_integer(start_sec, 24 * 3600)  # 시작 시간 ~ 23:59:59
        clock_integer(0, end_sec+1)  # 00:00:00 ~ 끝 시간 + 1
    if start_sec < end_sec:  # 끝 시간이 시작 시간보다 크다면,
        clock_integer(start_sec, end_sec+1)  # 시작 시간 ~ 끝 시간 + 1
    print(cnt)

# 문제 : https://www.acmicpc.net/problem/1942
