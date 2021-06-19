# 문제 풀이 아이디어
# 1. 문자열의 0과 1의 묶음을 개수로 센다.
# 2. 묶음의 개수 중 최솟값을 출력한다.
s = input()

cnt_1, cnt_0 = 0, 0
standard = s[0]  # 기준수 초기값
for num in s:
    if num != standard:  # 기준수와 달라지면 묶음 개수 +1
        if standard == '1':
            cnt_1 += 1
            standard = '0'
        else:
            cnt_0 += 1
            standard = '1'
    else:
        continue

# 위의 for문에서 마지막 묶음은 고려되지 않았다.
if standard == '1':
    cnt_1 += 1
else:
    cnt_0 += 1

print(min(cnt_1, cnt_0))

# 문제 : https://www.acmicpc.net/problem/1439
