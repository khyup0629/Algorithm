# 전형적인 KMP 알고리즘의 문제
# 실패함수를 이용한 KMP 알고리즘을 사용하면 된다.
T = input()
P = input()

# 실패함수
# P 문자열에 대해서 실패함수를 통해 각 위치까지의
# 접두부와 접미부가 같은 길이를 pi 테이블에 기록한다.
j = 0
pi = [0] * len(P)
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = pi[j - 1]
    if P[i] == P[j]:
        j += 1
        pi[i] = j

i = 0  # T와 P를 비교하는 시작점
j = 0  # P 문자열 위를 움직이는 인덱스
cnt = 0  # 같은 문자열의 갯수
firstIndex = []  # 같은 문자열이 나타나는 T기준 위치(인덱스+1)
while i+j < len(T):
    if T[i+j] != P[j]:
        if j == 0:  # 첫 인덱스부터 문자가 다르다면,
            i += 1
        else:
            # 시작점의 위치는 현재 위치(i)에서
            # 다른 문자 위치(j) - 접두부의 최대 길이(pi[j-1])
            # 만큼 더해주면(+) 된다.
            i += j - pi[j-1]
            # 접두부의 최대 길이가 곧 다음에 탐색할 j의 위치가 된다.
            # 위에서 시작점의 위치를 += j - pi[j-1]로 갱신했기 때문에
            # 접두부가 같은 만큼 시작위치(i)부터 같다.
            # 따라서, 앞에서부터 비교해줄 필요가 없고, 그 이후로 비교해주면 된다.
            j = pi[j-1]
    else:
        j += 1
        if j == len(P):
            cnt += 1
            firstIndex.append(i+1)
            i += j - pi[j - 1]
            j = pi[j - 1]

print(cnt)
for i in firstIndex:
    print(i, end=' ')

# 문제 : https://www.acmicpc.net/problem/1786

"""
(보충 설명)

    0123456789
T   ABCDABCDABDE
    ||||||X
P   ABCDABD
pi  0000120

- 다른 위치(6) 아래로 P의 문자열 중 접두부 최대 길이는 pi[6-1] = 2이다.
- 시작위치(i) += 다른 위치(6) - 접두부 최대 길이(pi[6-1]=2) = 4가 된다.

    0123456789
T   ABCDABCDABDE
        ||
P       ABCDABD
pi      0000120

- j의 위치는 시작위치를 새로 갱신할 때 접두부 최대 길이(pi[j-1])를 고려했으므로
시작위치(i)에서 접두부 최대 길이만큼은 당연히 일치하는 문자열이 된다.
- 따라서, j=0부터 고려할 필요 없이 j=pi[j-1]=2에서부터 고려할 수 있다.

예제 입력 2
ABBABCABCABDAA
ABC
예제 출력 2
2
4 7
"""
