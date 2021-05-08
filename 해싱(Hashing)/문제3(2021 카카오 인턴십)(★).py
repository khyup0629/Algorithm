# 정확도 100%
# 효율성 개선이 필요

from collections import defaultdict
# cmd 형식 : "U X" "D X" "C" "Z"
# n : 총 행 갯수, k : 시작 행 번호
n, k = 8, 1
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "Z", "Z"]


def solution(n, k, cmd):
    answer = ''
    table = defaultdict(int)
    for i in range(n):
        table[i] = i
    backup = []

    for i in range(len(cmd)):
        if len(cmd[i]) >= 3:  # 이동 명령이 들어왔을 경우
            direc, cnt = cmd[i][0], int(cmd[i][2:])
            if direc == 'D':
                for a in range(cnt):
                    k += 1
                    while k in backup:
                        k += 1
            elif direc == 'U':
                for a in range(cnt):
                    k -= 1
                    while k in backup:
                        k -= 1

        else:  # 삭제 또는 복구 명령이 들어왔을 경우
            del_or_backup = cmd[i][0]
            if del_or_backup == 'C':
                backup.append(k)  # 가장 최근 데이터 저장
                del table[k]
                k += 1  # 하나 위를 선택함으로써 그 자리에 있는 것처럼
                while k in backup:
                    k += 1
                if k == n:  # 맨 끝에 있으면,
                    k -= 1
                    while k in backup:
                        k -= 1
            else:
                x = backup.pop()
                table[x] = x  # 가장 최근에 삭제된 데이터 복구

    for i in range(n):
        if i in table:
            answer += 'O'
        else:
            answer += 'X'

    return answer


print(solution(n, k, cmd))