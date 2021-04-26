n = int(input())
array = []

for _ in range(n):
    string_lst = input()
    string_cnt = len(string_lst)
    array.append((string_lst, string_cnt))
# 중복 제거
array = list(set(array))  # 랜덤하게 정렬된다
# array 의 원소가 (0, 1) 형태로 있으면 1을 우선적으로 정렬 후 0을 정렬
array.sort(key=lambda word: (word[1], word[0]))

for i in array:
    print(i[0])

"""
n = int(input())

string_lst = [input() for _ in range(n)]

array = [[] for _ in range(51)]  # index : 0~50
for word in string_lst:
    if array[len(word)].count(word) == 0:
        array[len(word)].append(word)

for i in range(1, 51):
    array[i].sort()

result = []
for i in array:
    for j in i:
        result.append(j)

for i in result:
    print(i)
"""
