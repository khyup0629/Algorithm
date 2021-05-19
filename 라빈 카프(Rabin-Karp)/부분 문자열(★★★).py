# 라빈-카프 : 시간초과, KMP : 해결
# 배운 이론을 토대로 코드를 작성했으나 시간초과가 나는 이유를 알 수 없다.
# 코드상으로 O(n)이 소요되는 것 같은데 내가 간과한 무엇인가가 있는 것 같다.
# 같은 문자열인지 비교하는 for 같은 경우에는 해시값이 충돌하는 문자열이
# 거의 없기 때문에 웬만하면 한 번에 끝이 난다.
S = input()
P = input()

result = 0
value_S, value_P = 0, 0
n = len(P)
arr = [i for i in range(n-1, -1, -1)]
for i in range(n):
    value_P += (ord(P[i]) * (2 ** arr[i]))
    value_S += (ord(S[i]) * (2 ** arr[i]))

if value_S == value_P:
    result = 1
    for i in range(n):
        if S[i] != P[i]:
            result = 0
            break

start = 1
end = len(P)
while end < len(S):
    value_S = 2 * (value_S - ord(S[start-1]) * (2 ** arr[0])) + ord(S[end])
    if value_S == value_P:
        result = 1
        for i in range(n):
            if S[i+start] != P[i]:
                result = 0
                break
        if result:
            break
    start += 1
    end += 1

print(result)

# 문제 : https://www.acmicpc.net/problem/16916
