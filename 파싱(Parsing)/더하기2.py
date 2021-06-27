s = ''
while True:
    try:
        a = input()
        s += a
    except EOFError:
        break

print(sum(list(map(int, s.split(',')))))

# 문제 : https://www.acmicpc.net/problem/10823
