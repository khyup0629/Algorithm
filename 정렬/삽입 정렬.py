# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 첫 번째 원소는 이미 정렬이 되어 있다고 판단하고
# 그 이후 원소부터 바로 앞의 원소와 차례대로 비교해
# 자리를 바꿔주며 정렬

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
