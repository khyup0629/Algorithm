T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    array = input()
    lock = array + array
    rot = n // 4
    result = []
    for i in range(rot):
        temp = '0X'  # 16진수 대문자 접두어
        for j in range(n):
            temp += lock[n-i+j]
            if j % rot == rot - 1:
                if temp not in result:
                    result.append(temp)
                temp = '0X'

    for i in range(len(result)):
        # int('접두어 붙은 문자열', '문자열의 진수')
        result[i] = int(result[i], 16)  # 16진수 -> 10진수

    result.sort(reverse=True)
    print('#{0} {1}'.format(test_case, result[k-1]))

# 문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
