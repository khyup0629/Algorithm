'''
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

입력 조건 : 첫째 줄에 하나의 문자열 S가 주어집니다.(1 <= S의 길이 <= 10,000)
출력 조건 : 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

입력 예시 1
K1KA5CB7
출력 예시 1
ABCKK13

입력 예시 2
AJKDLSI412K4JSJ9D
출력 예시 2
ADDIJJJKKLSS20
'''

S = input()
result = []
value = 0
# i.isalpha()는 i가 알파벳인지 묻는 함수
# for i in S에서 S가 문자열이면 문자 하나하나가 i가 됨
for i in S:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()
# value = 0이면 결과값엔 아무것도 나타나선 안돼
# 0이 아니면 문자 뒤에 붙여준다
if value != 0:
    result.append(str(value))
# 리스트를 문자열로 변환하여 출력
# ''.join(리스트) : 리스트의 원소들을 공백없이 붙여서 문자열로 만듦
print(''.join(result))

'''
# 아이디어
# 1. 전체 문자열을 오름차순 정렬
# 2. 숫자는 원래 문자열에서 빼고 따로 값을 더함
# 3. 문자 + 숫자 순서대로 나열

S = input()

d = []
for i in range(len(S)):
    d.append(S[i])

d.sort()
result_number = 0
i = 0
while True:
    if ord(d[i]) < ord('A'):
        result_number += int(d[i])
        d.remove(d[i])
    else:
        break

for i in range(len(d)):
    print(d[i], end='')
print(result_number)
'''
