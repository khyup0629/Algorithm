from itertools import permutations

n = int(input())
arr = [i for i in range(1, n+1)]
permu = sorted(list(permutations(arr, n)))

for i in permu:
    for j in i:
        print(j, end=' ')
    print()

# 문제 : https://www.acmicpc.net/problem/10974
