string = input()
n = len(string)

hash_map = {}
for i in range(n):
    array = ''
    for j in range(i, n):
        array += string[j]
        # 중복되는 것은 자연스럽게 덮어씌움.
        hash_map[array] = 1

# 딕셔너리의 value 값들을 모두 더한다.
print(sum(hash_map.values()))

# 문제 : https://www.acmicpc.net/problem/11478
