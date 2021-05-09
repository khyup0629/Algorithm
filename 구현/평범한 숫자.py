T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    array = list(map(int, input().split()))
    cnt = 0

    for i in range(1, n-1):
        sel = array[i-1:i+2]
        _max, _min = max(sel), min(sel)
        if array[i] != _max and array[i] != _min:
            cnt += 1

    print('#', test_case, ' ', cnt, sep='')

# 문제 : https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
