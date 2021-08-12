# m = 1 : 2진수를 8자리로 맞춰준다.
# m = 2 : 2진수를 64자리로 맞춰준다.

t = int(input())

for _ in range(t):
    m, n = input().split()
    if m == '1':
        n = list(map(int, n.split('.')))
        ans = ''
        for i in range(len(n)):
            trans = str(format(n[i], 'b'))
            if len(trans) < 8:  # 부족한 만큼 0으로 채워줍니다.
                trans = '0' * (8 - len(trans)) + trans  # 2진수를 8자리로 맞춰줍니다.
            ans += trans  # 이어붙여서
        print(int(ans, 2))  # 10진수로 변환합니다.
    if m == '2':
        ans = []
        trans = str(format(int(n), 'b'))
        if 64 - len(trans) != 0:  # 2진수를 64자리로 맞춰줍니다.
            trans = '0' * (64 - len(trans)) + trans
        for i in range(0, len(trans), 8):  # 8자리씩 끊어서 10진수로 변환합니다.
            ans.append(str(int(trans[i:i+8], 2)))
        print('.'.join(ans))  # 사이에 '.'을 끼워넣고 합칩니다.

# 문제 : https://www.acmicpc.net/problem/12787
