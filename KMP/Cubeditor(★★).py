# 해싱으로 풀 경우 메모리 초과현상이 나타난다.
# 따라서, KMP 알고리즘을 공부해서 이용했다.
# 부분 문자열 : 부분 수열과는 다르게 투 포인터처럼 연속된 문자열이다.
string_i = input()
l = len(string_i)

array = []
for k in range(l):
    string = string_i[k:l]
    pi = [0] * len(string)
    j = 0
    for i in range(1, len(string)):
        # 이 부분이 이해가 안된다.
        while string[j] != string[i] and j != 0:
            j = pi[j-1]
        if string[j] == string[i]:
            j += 1
            pi[i] = j
    print(pi)
    array.append(max(pi))

print(max(array))

# 문제 : https://www.acmicpc.net/problem/1701

