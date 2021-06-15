data = []
while True:
    try:
        a = input()
        data.append(a)
    except EOFError:
        break

color_value = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
               'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
color_multi = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000, 'green': 100000,
               'blue': 1000000, 'violet': 10000000, 'grey': 100000000, 'white': 1000000000}
result = ''
for i in range(len(data)):
    if i == len(data) - 1:
        result = int(result) * color_multi[data[i]]
    else:
        result += str(color_value[data[i]])

print(result)

# 문제 : https://www.acmicpc.net/problem/1076
