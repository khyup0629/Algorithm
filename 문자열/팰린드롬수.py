while True:
    num = input()
    if num == '0':
        break

    n = len(num)
    fel = True
    for i in range(n//2):
        if num[i] != num[-(i+1)]:
            fel = False
            break

    if fel:
        print('yes')
    else:
        print('no')
