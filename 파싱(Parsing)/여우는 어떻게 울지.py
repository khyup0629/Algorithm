t = int(input())

for _ in range(t):
    growl = list(input().split())

    animal = []
    while True:
        goes = input()
        if goes == 'what does the fox say?':
            break
        sound = list(goes.split(' goes '))
        animal.append(sound[1])

    result = ''
    for i in growl:
        if i not in animal:
            result += (i + ' ')

    print(result)
    # ' '.join(result) 으로도 가능

# 문제 : https://www.acmicpc.net/problem/9536
