h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2

gap = time2 - time1
if gap <= 0:  # 적어도 1초를 기다리고, 많아야 24시간을 기다리므로 시간이 같을 때 24시간을 기다려야한다.
    gap += (24 * 3600)
h = str(gap // 3600)
if len(h) == 1:  # 'hh' 형태로 나타내기
    h = '0' + h
gap = gap % 3600
m = str(gap // 60)
if len(m) == 1:  # 'mm' 형태로 나타내기
    m = '0' + m
s = str(gap % 60)
if len(s) == 1:  # 'ss' 형태로 나타내기
    s = '0' + s

print('{0}:{1}:{2}'.format(h, m, s))

# 문제 : https://www.acmicpc.net/problem/3029
