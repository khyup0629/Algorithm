x = input()

if x[0] == '0' and x[1] == 'x':
    print(int(x[2:], 16))
elif x[0] == '0':
    print(int(x[1:], 8))
else:
    print(int(x))

# 문제 : https://www.acmicpc.net/problem/11816
