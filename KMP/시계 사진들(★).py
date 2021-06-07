# 원형으로 순환하는 문자열이 같은 지를 알아볼 때 KMP 를 사용한다.
# 1. 무작위로 기록된 바늘의 각도들을 정렬한다.(시간 복잡도에 영향을 미치지 않는다.)
# 2. 각 바늘 사이의 간격을 문자열처럼 만든다. (첫 번째 수열은 전체 문자열, 두 번째 수열은 부분 문자열)
# 3. 전체 문자열의 길이를 2배로 늘린다.
# 4. KMP 알고리즘을 통해 같은 문자열이 있는지 찾아본다.
import sys

input = sys.stdin.readline

n = int(input())

num_1 = list(map(int, input().split()))
num_2 = list(map(int, input().split()))

# 바늘을 순서대로 정렬한다.
num_1.sort()
num_2.sort()

string = []  # 전체 문자열
s = []  # 부분 문자열
# 각 바늘 사이의 간격을 문자열처럼 만든다.
for i in range(n):
    if i == n - 1:  # 처음과 끝 바늘 사이의 간격
        diff_1 = 360000 - (num_1[i] - num_1[0])
        diff_2 = 360000 - (num_2[i] - num_2[0])
    else:  # 첫 번째 바늘부터 순차적으로 바늘 사이의 간격
        diff_1 = num_1[i + 1] - num_1[i]
        diff_2 = num_2[i + 1] - num_2[i]

    string.append(diff_1)
    s.append(diff_2)

string = string * 2  # 전체 문자열에 해당하는 string 순환하기 때문에 2배로 늘려준다.

# 실패함수
pi = [0] * n
b = 0
for a in range(1, n):
    while b > 0 and s[a] != s[b]:
        b = pi[b - 1]
    if s[a] == s[b]:
        b += 1
        pi[a] = b

# KMP
i, j = 0, 0
result = 'impossible'
while i + j < len(string):
    if string[i + j] != s[j]:
        if j == 0:
            i += 1
        else:
            i += j - pi[j - 1]
            j = pi[j - 1]
    else:
        j += 1
    if j == n:
        result = 'possible'
        break

print(result)

# 문제 : https://www.acmicpc.net/problem/10266
