N = int(input())

if N >= 1 and N <= 99:
    print(N)
else:
    w = 0
    for i in range(100, N + 1):
        d = list(str(i))
        if (int(d[1]) - int(d[0])) == (int(d[2]) - int(d[1])):
            w += 1
    print(99 + w)
