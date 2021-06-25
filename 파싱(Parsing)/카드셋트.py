string = input()
s = ''
lst = []
PKHT = [13, 13, 13, 13]
GRESKA = False
for i in range(len(string)):
    s += string[i]
    if i % 3 == 2:
        if s in lst:
            GRESKA = True
            break
        lst.append(s)
        s = ''
    if i % 3 == 0:
        if string[i] == 'P':
            PKHT[0] -= 1
        elif string[i] == 'K':
            PKHT[1] -= 1
        elif string[i] == 'H':
            PKHT[2] -= 1
        else:
            PKHT[3] -= 1

if GRESKA:
    print('GRESKA')
else:
    for cnt in PKHT:
        print(cnt, end=' ')

# 문제 : https://www.acmicpc.net/problem/11507
